const accordionContainers = document.querySelectorAll('[data-role="accordion-container"]'); // All accordion containers
const accordionContents = document.querySelectorAll('[data-role="accordion-content"]'); // All accordion content
const accordionIconsClosed = document.querySelectorAll('[data-role="accordion-icon-closed"]'); // All accordion closed icons
const accordionIconsOpen = document.querySelectorAll('[data-role="accordion-icon-open"]'); // All accordion open icons

accordionContents.forEach((accordionContent) => {
    accordionContent.style.display = 'none'; // Hides all accordion contents
});

accordionIconsClosed.forEach((icon) => {
    icon.style.display = 'flex';
});

accordionIconsOpen.forEach((icon) => {
    icon.style.display = 'none';
});

accordionContainers.forEach((accordionContainer, index) => {
    accordionContainer.addEventListener('click', () => {
        if (accordionContents[index].style.display === 'flex') {
            // If the accordion is already open, close it
            accordionContents[index].style.display = 'none';
            accordionIconsClosed[index].style.display = 'flex';
            accordionIconsOpen[index].style.display = 'none';
        } else {
            // If the accordion is closed, open it
            accordionContents.forEach((accordionContent) => {
                accordionContent.style.display = 'none'; // Hides all accordion contents
            });

            accordionIconsClosed.forEach((accordionIcon) => {
                accordionIcon.style.display = 'flex'; // Resets all icon transforms to 0deg (default)
            });

            accordionIconsOpen.forEach((accordionIcon) => {
                accordionIcon.style.display = 'none';
            });

            accordionContents[index].style.display = 'flex'; // Shows accordion content
            accordionIconsClosed[index].style.display = 'none'; // Rotates accordion icon 180deg
            accordionIconsOpen[index].style.display = 'flex';
        }
    });
});

const searchInput = document.getElementById('searchInput');
const authorButtons = document.querySelectorAll('.author-list-view01');

searchInput.addEventListener('input', function() {
  const query = this.value.trim().toLowerCase();

  authorButtons.forEach(button => {
    const authorName = button.textContent.toLowerCase();
    if (authorName.includes(query)) {
      button.style.display = 'block';
    } else {
      button.style.display = 'none';
    }
  });
});

function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    if (section) {
        // If it exists, scroll to it
        section.scrollIntoView({ behavior: 'smooth' });
    } else {
        // If it doesn't exist, redirect to the appropriate page
        if (sectionId === 'About') {
            window.location.href = '/#About';
        } else if (sectionId === 'API') {
            window.location.href = '/#API';
        }
    }
}
