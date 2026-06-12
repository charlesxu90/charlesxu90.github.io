---
title: "Rosetta 使用"
subtitle: ""
date: 2026-04-21
draft: false
author: "Xiaopeng Xu"
description: "Rosetta 使用笔记：安装与常见蛋白质设计/建模流程。"
tags: ["Rosetta", "Protein Design", "Tutorial"]
categories: ["Technology"]
lightgallery: true
toc:
  enable: true
---

核心思想是 Rotamer


## 安装

Rosetta 可以从 RosettaCommons 上面下载源代码。但需要在本地做 Compile 后才能使用。相关介绍见：[https://www.rosettacommons.org/demos/latest/tutorials/install_build/install_build](https://www.rosettacommons.org/demos/latest/tutorials/install_build/install_build)。

```powershell
tar -xvzf rosetta[releasenumber].tar.gz # 解压压缩包
cd rosetta*/main/source # 打开源代码文件夹
./scons.py -j 20 mode=release bin # 用 scons 来生成 binary 文件，20为核数
```
默认 build 好后在 ./bin/ 文件夹中。

运行示例：

```powershell
${Rosetta_binary_path}/rosetta_scripts.default.linuxgccrelease -in:path:database ${Rosetta__db_path} -parser:protocol permeability_design.xml -in:file:s input.pdb -nstruct 100 -overwrite -beta_nov16 -packer_palette:extra_base_type_file d_packer_palette_hydrophobic.txt -corrections:beta_nov16 true
```
其中，最核心的是 XML 配置文件。


## CycPep_predict 环肽构象预测

我的项目是要做环状多肽设计，其中最重要的技术要点是做环状多肽结构的预测。调研了一圈，发现 Rosetta 中的预测功能比较简单也可靠。其他 AlphaFold 也是可选方法，但是并不准确，尤其是有多个可能的构象时。


相关介绍见：[https://www.rosettacommons.org/docs/latest/structure_prediction/simple_cycpep_predict](https://www.rosettacommons.org/docs/latest/structure_prediction/simple_cycpep_predict)

对应文章是： **Accurate de novo design of hyperstable constrained peptides.** ***Nature, 2016.***

### 简介

“simple_cycpep_predict” 主要用来快速采样由主链环化约束的小肽的闭合构象。

这些肽可以：

1. 由任何混合的 L-或D-氨基酸残基、无手性（achiral）氨基酸残基、肽酰胺（peptoid）残基 或 L-或D-寡尿素（oligourea）残基组成；

2. 可指定主链氢键的数量；

3. 可指定氨基酸形成二硫键，将使用 [TryDisulfPermutations](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/TryDisulfPermuationsMover) mover 对所有二硫键组合进行采样；

4. 可指定某些位置与交联剂交联（cross-link），此时使用 CrosslinkerMover 将交联剂放置在交联剂上；

5. 与使用 [Abinitio-Relax](https://www.rosettacommons.org/docs/latest/application_documentation/structure_prediction/abinitio-relax)  应用程序执行的采样不同，采样是片段独立的；也就是说，不需要已知结构的数据库 。

### 命令行示例

简单的调用示例：

```plain
/.../main/source/bin/simple_cycpep_predict.default.linuxgccrelease -cyclic_peptide:sequence_file inputs/seq.txt -cyclic_peptide:genkic_closure_attempts 1000 -cyclic_peptide:min_genkic_hbonds 2 -mute all -unmute protocols.cyclic_peptide_predict.SimpleCycpepPredictApplication -in:file:native inputs/native.pdb -out:file:silent output.silent
```
可以通过 MPI 多进程来在超算上做构象 (conformation) 采用。示例：
```plain
mpirun -np 25 /.../main/source/bin/simple_cycpep_predict.mpi.linuxgccrelease -cyclic_peptide:MPI_processes_by_level 1 24 -cyclic_peptide:MPI_batchsize_by_level 10 -cyclic_peptide:MPI_output_fraction 0.1 -nstruct 2500 -cyclic_peptide:sequence_file inputs/seq.txt -cyclic_peptide:genkic_closure_attempts 1000 -cyclic_peptide:min_genkic_hbonds 2 -mute all -unmute protocols.cyclic_peptide_predict.SimpleCycpepPredictApplication_MPI_summary -in:file:native inputs/native.pdb -out:file:silent output.silent
```
多进程详情可以查看：[Build Documentation](https://www.rosettacommons.org/docs/latest/build_documentation/Build-Documentation)  of MPI。

### 核心参数：

* **-cyclic_peptide:sequence_file <filename>**  序列文件，必须参数。例如：PHE LYS ARG DLEU DASP DALA TYR ASN。

* **-cyclic_peptide:cyclization_type <string>** 环化类型，可选参数。 选项包括： "n_to_c_amide_bond" (default), "terminal_disulfide", "thioether_lariat", "nterm_isopeptide_lariat", "cterm_isopeptide_lariat", and "sidechain_isopeptide"。

* **-cyclic_peptide:use_chainbreak_energy <bool>** 默认为 true, 通过 N-to-C amide bond 环化，否则添加其他 constraints。

* **-out:nstruct <int>** 生成的构象数目。由于约束条件的限制，实际输出的结果会小于所设数值。

* **-cyclic_peptide:genkic_closure_attempts <int>** 对每一个结构，做 GenKIC 构象优化的次数，默认 10,000，建议 250 to 50,000。

* **-cyclic_peptide:genkic_min_solution_count <int>**  默认为 1。对每个结构，达到最大优化次数（**genkic_closure_attempts**）或已找到足够的结果数量（**genkic_min_solution_count**）；此时会选择最小能态的结果。

* **-cyclic_peptide:cyclic_permutations <bool>** If true (the default setting), then random cyclic permutations of the sequence are used to avoid biases introduced by the choice of cutpoint. (For example, if the user provides "ALA LYS PHE ASP DILE PRO", then we might try "PHE ASP DILE PRO ALA LYS" for the first structure, "DILE PRO ALA LYS PHE ASP" for the second, etc.) All structures are de-permuted prior to final output for easy alignment.

* **-cyclic_peptide:use_rama_filter <bool>** The kinematic closure algorithm uses three "pivot residues" to close the loop. These pivot residues can end up with nonsensical phi and psi values. If this flag is set to true (the default setting), then pivot residues for all solutions are filtered and solutions with poor Ramachandran scores are discarded.

* **-cyclic_peptide:rama_cutoff <float>** If the **use_rama_filter** option is true (the default), then solutions with pivot residues with Ramachandran scores above this value will be discarded. Defaults to 0.8 (somewhat permissive).

* **-cyclic_peptide:default_rama_sampling_table <string>** By default, mainchain torsion sampling for alpha-amino acids is biased by the Ramachandran map for the residue in question. This option allows the user to specify a custom Ramachandran map that will be used for sampling (unless the **-rama_sampling_table_by_res** option is used to override this flag). Not used if not specified. Current supported custom maps include: flat_l_aa_ramatable, flat_d_aa_ramatable, flat_symm_dl_aa_ramatable, flat_symm_gly_ramatable, flat_symm_pro_ramatable, flat_l_aa_ramatable_stringent, flat_d_aa_ramatable_stringent, flat_symm_dl_aa_ramatable_stringent, flat_symm_gly_ramatable_stringent, and flat_symm_pro_ramatable_stringent.

* **-cyclic_peptide:rama_sampling_table_by_res <integer> <string> <integer> <string> ...** This flag allows the user to specify a custom Ramachandran to be used for sampling, by amino acid residue. For example, "-cyclic_peptide:rama_sampling_table_by_res 3 flat_symm_pro_ramatable 4 flat_d_aa_ramatable_stringent" will assign a symmetric proline table to residue 3 and a high-stringency d-amino acid table to residue 4. Not used if not specified.

* **-cyclic_peptide:use_classic_rama_for_sampling <bool>** If true, the `rama` score term's Ramachandran maps are used to bias sampling instead of the newer `rama_prepro` score term's Ramachandran maps. Not recommended. Default false.

* **-cyclic_peptide:min_genkic_hbonds <int>** This is the minimum number of mainchain hydrogen bonds that a tentatively-considered closure solution must have in order to avoid rejection. Default 3. If this is set to 0, the hydrogen bond criterion is not applied.

* **-cyclic_peptide:min_final_hbonds <int>** This is the minimum number of mainchain hydrogen bonds that a final closure solution must have post-relaxation in order to avoid rejection. This defaults to 0 (which means that the final number of hydrogen bonds is reported, but is not used as a filter).

* **-cyclic_peptide:total_energy_cutoff <float>** The maximum total score, above which solutions are discarded. Not used if not specified (*i.e.* solutions of any energy are accepted).

* **-cyclic_peptide:hbond_energy_cutoff <float>** The maximum hydrogen bond energy, above which a hydrogen bond is not counted. Defaults to -0.25.

* **-cyclic_peptide:do_not_count_adjacent_res_hbonds <bool> When counting hydrogen bonds, should we ignore hydrogen bonds between adjacent residues? Default true.**

* ****-cyclic_peptide:high_hbond_weight_multiplier <float>** For portions of the protocol that perform relaxation with an upweighted mainchain hydrogen bond score value (see the algorithm description, below), this is the factor by which the mainchain hydrogen bond score term is upweighted. Defaults to 10.0 (tenfold increase).

* **-cyclic_peptide:count_sc_hbonds <bool>** Should sidechain-mainchain hydrogen bonds be counted as mainchain hydrogen bonds? Defaults to false.

* **-cyclic_peptide:fast_relax_rounds <int>** At steps of the protocol at which relaxation is invoked, this is the number of rounds of the [FastRelax](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/FastRelaxMover) protocol that will be applied. Defaults to 3.

* **-cyclic_peptide:exclude_residues_from_rms <string>** A space-separated list of residues that should be excluded from the RMSD calculation. Not used if not provided.

* **-cyclic_peptide:checkpoint_job_identifier <string>** If this option is used, jobs will checkpoint themselves so that the **minirosetta** or **simple_cycpep_predict** apps can be interrupted and can pick up where they left off, without repeating failed jobs or re-doing successful jobs. The string must be a unique session identifier used to distinguish between re-attempts of the current prediction or new runs. Highly recommended for BOINC jobs.

* **-cyclic_peptide:rand_checkpoint_file <string>** If the **-checkpoint_job_identifier** flag is used, this flag sets the name of the checkpoint file used for the random number generator. Defaults to "rng.state.gz" if not specified. Typically, this need only be specified if multiple checkpointed jobs are sharing the same working directory.

* **-cyclic_peptide:checkpoint_file <string>** If the **-checkpoint_job_identifier** flag is used, this flag sets the name of the checkpoint file used for keeping track of what jobs have completed and what jobs still have to run. Defaults to "checkpoint.txt" if not specified. Typically, this need only be specified if multiple checkpointed jobs are sharing the same working directory.

* **-cyclic_peptide:require_disulfides <bool>** If true, then the application attempts to form disulfides between all disulfide-forming residues, trying permutations using the [TryDisulfPermutations](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/TryDisulfPermuationsMover) mover. False by default.

* **-cyclic_peptide:disulf_cutoff_prerelax <Real>** If require_disulfides is true, this is the maximum disulfide energy per disulfide bond that is allowed prior to relaxation. If the energy exceeds this value, the solution is rejected. Default is 15.0, but a much larger value might be appropriate.

* **-cyclic_peptide:disulf_cutoff_postrelax <Real>** If require_disulfides is true, this is the maximum disulfide energy per disulfide bond that is allowed following relaxation. If the energy exceeds this value, the solution is rejected. Default 0.5.

* **-cyclic_peptide:user_set_alpha_dihedrals <RealVector>** Optionally, the user may fix certain mainchain dihedrals at user-specified values. This flag must be followed by a list of groups of four numbers, in which the first represents a sequence position and the second, third, and fourth are the phi, psi, and omega values, respectively. Unused if not specified. Note that this only works for alpha-amino acids and peptoids.

* **-cyclic_peptide:user_set_alpha_dihedral_perturbation <Real>** If the **user_set_alpha_dihedrals** option is used, this is a small gaussian perturbation added to all dihedrals that were set. Default 0.

* **-in:file:native <pdb_filename>** A PDB file for the native structure. Optional. If provided, an RMSD value will be calculated for each generated structure.

* **-cyclic_peptide:filter_oversaturated_hbond_acceptors <bool>** Should sampled conformations with more than the allowed number of hydrogen bonds to an acceptor be discarded? Default true.

* **-cyclic_peptide:hbond_acceptor_energy_cutoff <Real>** If we are filtering out conformations with oversaturated hydrogen bond acceptors, this is the hydrogen bond energy threshold above which a hydrogen bond is not counted. Default -0.1.

* **-cyclic_peptide:sample_cis_pro_frequency <Real>** This option controls the frequency (between 0 and 1) with which *cis*-peptide bonds are sampled for residues preceding D- or L-proline. If the option is not specified, the frequency defaults to 0.3; set it to 0.0 to disable *cis*-peptide bond sampling. Note that this is based on the input sequence, and is not recommended for design unless certain positions are fixed to be proline.

* **-cyclic_peptide:angle_relax_rounds <int>** If this option is used, the specified number of FastRelax or FastDesign rounds is carried out with flexible bond angles. The cart_bonded energy is automatically set to 0.5 for this step, and the pro_close energy to 0.0. The order of operations is: ordinary FastRelax (if any), flexible bond angle FastRelax (if any), flexible bond angle / bond length FastRelax (if any), full Cartesian FastRelax (if any), and one more round of regular FastRelax (only if any rounds were specified that could result in non-ideal bond angles or bond lengths). Default behaviour is to have no rounds of flexible bond angle relaxation.

* **-cyclic_peptide:angle_length_relax_rounds <int>** If this option is used, the specified number of FastRelax or FastDesign rounds is carried out with flexible bond angles and flexible bond lengths. The cart_bonded energy is automatically set to 0.5 for this step, and the pro_close energy to 0.0. Default behaviour is to have no rounds of flexible bond angle / bond length relaxation. See note above for order of relaxation rounds.

* **-cyclic_peptide:cartesian_relax_rounds <int>** If this option is used, the specified number of FastRelax or FastDesign rounds is carried out with full Cartesian-space minimization. The cart_bonded energy is automatically set to 0.5 for this step, and the pro_close energy to 0.0. Default behaviour is to have no rounds of Cartesian-space relaxation. See note above for order of relaxation rounds.

* **-out:file:o <pdb_filename>** OR **-out:file:silent <silent_filename>** Prefix for PDB files that will be written out, OR name of the binary silent file that will be generated.

### 输出结果

This application generates PDB or binary silent file output. If the latter is used (recommended), hydrogen bond counts and RMSD values to native (if a native file was provided) are in the `SCORE` lines in the silent file. Additionally, these values are reported in the output log.

The BOINC compilation also has some groovy graphics.

### 算法

The algorithm is as follows:

1. For each sampling attempt, the application generates a linear peptide with the given sequence (randomly circularly permuted if the **-cyclic_peptide:cyclic_permutations** flag is set to true, the default). The starting conformation is randomized, with each residue's phi/psi pair biased by the Ramachandran plot for that residue type. All omega angles are set to 180 degrees.

2. The [Generalized Kinematic Closure](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/GeneralizedKICMover) (GenKIC) protocol is used to find closed (cyclic) conformations of the peptide. A single residue is chosen at random to be an "anchor" residue (excluding the two end residues). The rest of the peptide is now a giant loop to be closed with GenKIC. The first, last, and a randomly-chosen middle residue are selected as "pivot" residues. GenKIC performs a series of samples (up to a maximum specified with the **-cyclic_peptide:genkic_closure_attempts** flag) in which it:

   1. 2a. Randomizes all residues in the loop, biased by the Ramachandran map.

   2. 2b. Analytically solves for phi and psi values for the pivot residues to close the loop. At this step, anywhere from 0 to 16 solutions might result from the linear algebra performed.

   3. 2c. Filters each solution based on internal backbone clashes, the Ramachandran score for the pivot residues (controlled with the **-cyclic_peptide:rama_cutoff** flag), the presence of oversaturated hydrogen bond acceptors (controlled with the **-cyclic_peptide:filter_oversaturated_hbond_acceptors** flag), and the number of backbone hydrogen bonds (controlled with the **-cyclic_peptide:min_genkic_hbonds** flag). Solutions passing all filters are relaxed using [FastRelax](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/FastRelaxMover) with an elevated hydrogen bond weight (set using the **-cyclic_peptide:high_hbond_weight_multiplier** flag), then stored. (Note that the user can specify multiple rounds of ordinary FastRelax, flexible bond angle FastRelax, flexible bond angle / bond length FastRelax, or Cartesian FastRelax. These are applied in this order. Note, too, that FastDesign can be substituted for FastRelax at this stage -- see the section below on design for more information.)

   4. 2d. Repeats 2a through 2c until the maximum number of samples is reached, or until GenKIC has stored the number of solutions (passing filters) specified with the **-cyclic_peptide:genkic_min_solution_count** flag.

   5. 2e. Chooses the lowest-energy solution, based on the scorefunction with the exaggerated hydrogen bonding weight.

3. The resulting solution is then relaxed using the conventional scorefunction (hydrogen bond weight reset to normal value). Again, the user may request multiple rounds of ordinary FastRelax, flexible bond angle FastRelax, flexible bond angle / bond length FastRelax, or full Cartesian FastRelax; these are carried out in this order. If any form of FastRelax is used that can perturb bond angles or bond lengths from ideal values, a final round of ordinary FastRelax is also appended at the very end.

4. A final hydrogen bond filter is applied (controlled with the **-cyclic_peptide:min_final_hbonds** flag).

5. The structure, if one is found, is written to disk, and the application proceeds to the next attempt until the number of attempts specified with the **-out:nstruct** flag is reached.

Optionally, step 2c can be performed with [FastDesign](https://www.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/Movers/movers_pages/FastDesignMover) instead of FastRelax. See the section on design, below, for more information about this.

### 通过 MPI 在超算上进行采样

When Rosetta is compiled with the "extras=mpi" flag, the compiled version of the **simple_cycpep_predict** app (bin/simple_cycpep_predict.mpi.[os][compiler][release/debug]) has some additional features, with additional flags controlling those features. In MPI mode, the app has a custom-written scalable job distribution and collection system, suitable for parallel sampling on systems as small as a laptop or as large as the IBM Blue Gene/Q infrastructure (hundreds of thousands of parallel CPUs). The compilation flags "extras=cxx11thread,mpi" will also enable multi-threaded parallelism within a computing node, and multi-process parallelism with jobs distributed by MPI between nodes. This is covered in detail in the next section.

The job distribution system consists of a single **director** process, an arbitrary number of levels of **intermediate manager** processes that send information up and down the hierarchy, and a large number of **worker** processes that actually do the sampling work. (Note that these layers were formerly called "emperor", "master", and "slave", and may appear as such in older versions of Rosetta.) Each level in the hierarchy has a number of nodes greater than or equal to its parent level. The number of nodes in the hierarchy is specified with the **-cyclic_peptide:MPI_processes_by_level** flag, followed by a series of whitespace-separated integers representing the number of processes at each level, starting with the director and ending with the workers. The sum of these numbers must equal the total number of MPI processes launched. For example, the following would specify one director, 50 intermediate managers (in a single level of intermediate managers), and 4949 workers, for a total of 5000 processes (the same number launched):

```plain
mpirun -np 5000 /my_rosetta_path/main/source/bin/simple_cycpep_predict.mpi.linuxgccrelease -cyclic_peptide:MPI_processes_by_level 1 50 4949 ...(other options)...
```
In the above, the workers would be assigned to managers to make the distribution as even as possible. Since two-level distribution is very common, with one director talking to N-1 workers (given N total processes), one may use the **-cyclic_peptide:MPI_auto_2level_distribution** flag in lieu of the **-cyclic_peptide:MPI_processes_by_level** flag to set this up. The **-cyclic_peptide:MPI_auto_2level_distribution** takes no options.
At the start of a run, workers send requests for jobs up the hierarchy. Jobs are distributed to each level of the hierarchy in batches, with user-controlled batch sizes. If batches are too small, the risk is that nodes spend all of their time requesting jobs and responding to job requests; if they are too large, the risk is that workers are locked in to completing a large number of jobs even if another worker is free to do those jobs (*i.e.* poor load-balancing). The number of jobs per batch at each level of the hierarchy is controlled with the **-cyclic_peptide:MPI_batchsize_by_level** flag, followed by a whitespace-separated list of integers. One less value should be provided than was provided with the **-cyclic_peptide:MPI_processes_by_level** flag, since workers do not pass batches of jobs any further down the hierarchy. Using the example above, we could specify that the director would send out 200 jobs at a time to each manager, and that each manager would send 2 jobs at a time to each worker, with the following:

```plain
mpirun -np 5000 /my_rosetta_path/main/source/bin/simple_cycpep_predict.mpi.linuxgccrelease -cyclic_peptide:MPI_processes_by_level 1 50 4949 -cyclic_peptide:MPI_batchsize_by_level 200 2 ...(other options)...
```
The total number of jobs is controlled with the **-nstruct** flag. One may also trigger premature termination using the **-cyclic_peptide:MPI_stop_after_time <Integer>** flag, and specifying a time in seconds. If this flag is used, then after the elapsed time, the director will send a halt signal down the hierarchy. Slaves that have been assigned jobs will complete all jobs assigned to them, but no subsequent jobs will be assigned to them. This is useful for large-scale sampling on systems that have job time limits.
When jobs complete, they are not output automatically, since there might be far more output than could be reasonably written out to disk. Instead, the workers send job summaries up the hierarchy. These are sorted during passage up the hierarchy by a criterion specified by the user using the **-cyclic_peptide:MPI_sort_by <criterion>** flag, where <criterion> is one of **energy**, **rmsd**, or **hbonds**. By default, lowest values are first in the list, but this can be changed with **-cyclic_peptide:MPI_choose_highest true**. The director node receives the sorted list, then sends requests down the hierarchy to the originating nodes for only the top N% (based on the sort criterion) of output structures, which are sent up the hierarchy to the director for output to disk. The fraction of structures written to disk is set with the **-cyclic_peptide:MPI_output_fraction** flag, with a value from 0 to 1. So if we wanted to do 20,000 samples, then write out the 5% of output structures with lowest energy from the run in the example above, we would use:

```plain
mpirun -np 5000 /my_rosetta_path/main/source/bin/simple_cycpep_predict.mpi.linuxgccrelease -cyclic_peptide:MPI_processes_by_level 1 50 4949 -cyclic_peptide:MPI_batchsize_by_level 200 2 -nstruct 20000 -cyclic_peptide:MPI_sort_by energy -cyclic_peptide:MPI_output_fraction 0.05 ...(other options)...
```
The details of sampling are controlled with the same flags used for the non-MPI version (see above).
Note that, in MPI mode, there can be an incredible amount of tracer output. For convenience, the director uses a separate tracer to write a summary of all jobs that have been completed. This summary includes the energy of each sample, the RMSD to native (if a native structure was provided), and a goodness-of-funnel metric (PNear). Optionally, RMSD and PNear values may also be computed to the lowest-energy sample (rather than to a user-provided native). To enable this, use the **-cyclic_peptide:compute_rmsd_to_lowest** option. Alternatively, RMSD and PNear values may be compued to the lowest-energy N% of samples. To enable this, use the **-cyclic_peptide:compute_pnear_to_this_fract xxx** option, where xxx is a value from 0.0 to 1.0 representing the fraction of samples to which PNear should be calculated.

The PNear metric takes two parameters: **lambda** in Angstroms, which controls how close a sample has to be to native to be considered native-like, and **Boltzmann temperature** in Rosetta energy units, which controls how high-energy a non-native sample must be for the funnel not to be considered "bad". These are set with the **-cyclic_peptide:MPI_pnear_lambda** and **-cyclic_peptide:MPI_pnear_kbt** flags, respectively. See Bhardwaj, Mulligan, Bahl, *et al.* (2016) *Nature*, in press for more information about the PNear metric.

Optionally, the solvent-accessible surface areas of each sample, and of the Boltzmann-weighted ensemble, can be computed. To enable this, use the **-cyclic_peptide:compute_ensemble_sasa_metrics** option. Polar SASA, apolar SASA, and total SASA are all included in the output summary.

To receive only this summary as output in the standard output stream, use the **-mute all -unmute protocols.cyclic_peptide_predict.SimpleCycpepPredictApplication_MPI_summary** flags. (This silences all output from non-director processes, and most output from the director process, except for the summary at the end.) Since generating output and managing output from large numbers of processes takes clock and MPI communication cycles, muting unnecessary output is advised for better performance.

Note too that intermediate manager processes are optional; the minimum that one needs are an director node and a single worker node (though this setup would have no advantages over sampling with the non-MPI version of the app). On a 4-core laptop, the following would be perfectly legal, for example:

```plain
mpirun -np 4 /my_rosetta_path/main/source/bin/simple_cycpep_predict.mpi.linuxgccrelease -cyclic_peptide:MPI_processes_by_level 1 3 -cyclic_peptide:MPI_batchsize_by_level 25 -nstruct 1000 -cyclic_peptide:MPI_sort_by energy -cyclic_peptide:MPI_output_fraction 0.05 ...(other options)...
```
This would farm out 1000 jobs to 3 worker processes in 25-job batches, with direct communication between the director and each worker (i.e. no intermediate managers). This is inadvisable on very large systems, since the director can become inundated with too many communication requests from thousands of workers, but is sensible on small systems.
#### Using MPI- and thread-based parallelism on HPC clusters

When compiled with the flags "extras=cxx11thread,mpi", the **simple_cycpep_predict** application can make use of both process-based parallelism (with jobs distributed by MPI) and thread-based parallelism (with concurrent threads that share a memory space executing jobs simultaneously). The hierarchy described in the previous section gains a final level: an director distributes jobs to some number of layers of intermediate managers, which distribute jobs to some number of worker processes, which launch some number of worker threads within a node to carry out jobs in parallel. The **-cyclic_peptide:threads_per_worker** commandline option specifies the number of worker threads each worker process can launch. Note that a value of 1 results in no worker threads being launched; in this case, the behaviour is identical to the pure MPI-based job distribution. Higher values result in worker threads, with the caveat that N-1 threads will be used as workers, with the remaining thread reserved for MPI communication and job management. These threads will share a memory space, including a single copy of the Rosetta database loaded by the process into memory (resulting in considerable memory savings on an HPC node with limited memory and abundant CPUs). Given an HPC cluster with L nodes, M CPUs per node, and N cores per CPU, it is recommended to launch a total of L processes (one per node), and M*N threads per process. Note that if M*N is large, there may be some efficiency lost compared to pure MPI-based performance, however; in this case, the balance between memory usage and performance must determine the number of processes launched per node and the number of threads per process.

## FlexPepDock 多肽受体结合预测

### 简介

之前也看到了这个工具，但是觉得可能不太适合，只是优化。后来看到裴德华老师的一篇文章，才确定这个方法是可以用的。

FlexPepDock 包括了三类应用场景，结合构象优化 refinement，从头预测 ab-initio，和 全局预测 PIPER-FlexPepDock。目前看 ab-initio 和 PIPER-FlexPepDock 比较贴近我的使用场景。

### Refinement protocol:

```plain
Raveh B*, London N* and Schueler-Furman O
Sub-angstrom Modeling of Complexes between Flexible Peptides and Globular Proteins.
Proteins, 78(9):2029–2040 (2010).
```
Refinement 适用于可以使用近似的粗粒度交互模型的情况。 除了动态侧链优化之外，该协议还迭代优化肽主链及其相对于受体蛋白的刚体方向。

### *ab-initio* protocol:

```plain
Raveh B, London N, Zimmerman L and Schueler-Furman O
Rosetta FlexPepDock ab-initio: Simultaneous Folding, Docking and Refinement of Peptides onto Their Receptors.
PLoS ONE, 6(4): e18934 (2011).
```
*ab-initio* 大大扩展了Refinement方案，适用于没有有关肽主链构象的信息的情况。 它同时将肽折叠并停靠在受体表面上，从任意（例如，延伸的）主链构象开始。 假设肽最初定位在正确的结合位点附近，但该方案对于精确的起始方向是稳健的。

PIPER-FlexPepDock (Global docking protocol):

```plain
Alam N, Goldstein O, Xia B, Porter KA, Kozakov D, Schueler-Furman O 
High-resolution global peptide-protein docking using fragments-based PIPER-FlexPepDock. PLoS Comput Biol 13(12): e1005905 (2017).
```
PIPER-FlexPepDock 专为结合位点未知的情况而设计，从 PDB 格式的受体和仅肽序列开始。 代表肽构象整体的一组片段是与受体对接的刚体，并通过精炼方案进一步精炼至高分辨率。

 

## 相关用例
