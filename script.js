document.addEventListener('DOMContentLoaded', function() {
    const releasesContainer = document.getElementById('releases');

    fetch('https://api.github.com/repos/Aarnav-Tech/qrcode-gen/releases')
        .then(response => response.json())
        .then(data => {
            data.forEach(release => {
                const releaseItem = document.createElement('div');
                releaseItem.className = 'list-group-item';
                releaseItem.innerHTML = `
                    <div>
                        <strong>${release.name}</strong>
                        <div>${marked(release.body)}</div>
                    </div>
                `;

                // Check if there are assets to download
                if (release.assets.length > 0) {
                    release.assets.forEach(asset => {
                        const downloadButton = document.createElement('a');
                        downloadButton.href = asset.browser_download_url;
                        downloadButton.className = 'btn btn-primary btn-sm';
                        downloadButton.download = asset.name; // Set the download attribute to the asset name
                        downloadButton.textContent = `Download ${asset.name}`;
                        releaseItem.appendChild(downloadButton);
                    });
                } else {
                    const noAssetsMessage = document.createElement('p');
                    noAssetsMessage.className = 'no-assets';
                    noAssetsMessage.textContent = 'No downloadable assets available.';
                    releaseItem.appendChild(noAssetsMessage);
                }

                const viewButton = document.createElement('a');
                viewButton.href = release.html_url;
                viewButton.className = 'btn btn-secondary btn-sm';
                viewButton.target = '_blank';
                viewButton.textContent = 'View Release';
                releaseItem.appendChild(viewButton);

                releasesContainer.appendChild(releaseItem);
            });
        })
        .catch(error => {
            console.error('Error fetching releases:', error);
            releasesContainer.innerHTML = '<p class="text-danger">Failed to load releases.</p>';
        });
});
