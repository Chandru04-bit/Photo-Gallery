/**
 * PROJECT 58 – UTSAV STAGE, TENT & PANDAL CONTRACTOR
 * Forms Helper Script (forms.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Pre-select package or service if passed via URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const packageParam = urlParams.get('package');
  const serviceParam = urlParams.get('service');

  const packageSelect = document.getElementById('budgetRange') || document.getElementById('pricingPackage');
  const eventTypeSelect = document.getElementById('eventType');

  if (packageParam && packageSelect) {
    const matchingOption = Array.from(packageSelect.options).find(opt => 
      opt.value.toLowerCase().includes(packageParam.toLowerCase()) || 
      opt.text.toLowerCase().includes(packageParam.toLowerCase())
    );
    if (matchingOption) {
      packageSelect.value = matchingOption.value;
    }
  }

  if (serviceParam && eventTypeSelect) {
    const matchingService = Array.from(eventTypeSelect.options).find(opt => 
      opt.value.toLowerCase().includes(serviceParam.toLowerCase()) || 
      opt.text.toLowerCase().includes(serviceParam.toLowerCase())
    );
    if (matchingService) {
      eventTypeSelect.value = matchingService.value;
    }
  }

  // Password Show / Hide toggle
  const togglePasswordBtns = document.querySelectorAll('.password-toggle-btn');
  togglePasswordBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const targetInputId = this.getAttribute('data-target');
      const input = document.getElementById(targetInputId) || this.previousElementSibling;
      if (!input) return;

      const icon = this.querySelector('i');
      if (input.type === 'password') {
        input.type = 'text';
        if (icon) {
          icon.classList.remove('bi-eye');
          icon.classList.add('bi-eye-slash');
        }
      } else {
        input.type = 'password';
        if (icon) {
          icon.classList.remove('bi-eye-slash');
          icon.classList.add('bi-eye');
        }
      }
    });
  });

  // Set minimum date to today for datepicker inputs
  const eventDateInputs = document.querySelectorAll('input[type="date"]');
  const today = new Date().toISOString().split('T')[0];
  eventDateInputs.forEach(input => {
    input.setAttribute('min', today);
  });
});
