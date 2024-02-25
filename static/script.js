const accordionContainers = document.querySelectorAll('[data-role='accordion-container']'); // All accordion containers
               const accordionContents = document.querySelectorAll('[data-role='accordion-content']'); // All accordion content
               const accordionIconsClosed = document.querySelectorAll('[data-role='accordion-icon-closed']'); // All accordion closed icons
               const accordionIconsOpen = document.querySelectorAll('[data-role='accordion-icon-open']'); // All accordion open icons

               accordionContents.forEach((accordionContent) => {
                   accordionContent.style.display = 'none'; //Hides all accordion contents
               });

               accordionIconsClosed.forEach((icon) => {
                 icon.style.display = 'flex'
               })

               accordionIconsOpen.forEach((icon) => {
                 icon.style.display = 'none'
               })

               accordionContainers.forEach((accordionContainer, index) => {
                   accordionContainer.addEventListener('click', () => {
                       if (accordionContents[index].style.display === 'flex') {
                           // If the accordion is already open, close it
                           accordionContents[index].style.display = 'none';
                           accordionIconsClosed[index].style.display = 'flex';
                           accordionIconsOpen[index].style.display = 'none'
                       } else {
                           // If the accordion is closed, open it
                           accordionContents.forEach((accordionContent) => {
                               accordionContent.style.display = 'none'; //Hides all accordion contents
                           });

                           accordionIconsClosed.forEach((accordionIcon) => {
                               accordionIcon.style.display = 'flex'; // Resets all icon transforms to 0deg (default)
                           });

                           accordionIconsOpen.forEach((accordionIcon) => {
                             accordionIcon.style.display = 'none';
                           })

                           accordionContents[index].style.display = 'flex'; // Shows accordion content
                           accordionIconsClosed[index].style.display = 'none'; // Rotates accordion icon 180deg
                           accordionIconsOpen[index].style.display = 'flex';
                       }
                   });
               });