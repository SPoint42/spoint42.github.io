document.addEventListener("DOMContentLoaded", function() {
    const username = 'Spoint42'; // Remplacez par votre nom d'utilisateur GitHub
    const token = 'votre-token-github'; // Remplacez par votre token GitHub

    fetch(`https://api.github.com/users/${username}`, {
        headers: {
            Authorization: `token ${token}`
        }
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('github-followers').textContent = data.followers;
            document.getElementById('github-following').textContent = data.following;
            document.getElementById('github-repos').textContent = data.public_repos;
        })
        .catch(error => console.error('Error fetching GitHub data:', error));
});