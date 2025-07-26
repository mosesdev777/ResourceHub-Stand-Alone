
// JavaScript to handle the modal visibility
const deleteModal = document.getElementById('delete-modal');
const openModalBtn = document.getElementById('open-delete-modal');
const closeModalBtn = document.getElementById('close-delete-modal');

if (openModalBtn) {
    openModalBtn.addEventListener('click', () => {
        deleteModal.classList.remove('hidden');
    });
}

if (closeModalBtn) {
    closeModalBtn.addEventListener('click', () => {
        deleteModal.classList.add('hidden');
    });
}

// Close modal if user clicks outside of the modal content
window.addEventListener('click', (event) => {
    if (event.target === deleteModal) {
        deleteModal.classList.add('hidden');
    }
});
