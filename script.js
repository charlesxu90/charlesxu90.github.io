fetch('content.json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('name').innerText = data.name;
        document.getElementById('home-text').innerText = data.home;

        const researchList = document.getElementById('research-list');
        data.research.forEach(item => {
            let li = document.createElement('li');
            li.textContent = item;
            researchList.appendChild(li);
        });

        const publicationsList = document.getElementById('publications-list');
        data.publications.forEach(item => {
            let li = document.createElement('li');
            li.textContent = item;
            publicationsList.appendChild(li);
        });

        const awardsList = document.getElementById('awards-list');
        data.awards.forEach(item => {
            let li = document.createElement('li');
            li.textContent = item;
            awardsList.appendChild(li);
        });
    })
    .catch(error => console.error('Error loading content:', error));

