/**
 * PROJECT 58 – UTSAV STAGE, TENT & PANDAL CONTRACTOR
 * Strict Form Validation & Input Formatting Script (validation.js)
 * 
 * Enforces:
 *  1. Letters ONLY on Name and Location fields (numbers and symbols strictly blocked on keydown, input, paste).
 *  2. Numbers ONLY on Phone fields (letters and symbols strictly blocked, max 10 digits, validated for Indian mobile 6-9).
 *  3. Email validation with standard pattern.
 *  4. Future-only datepicker enforcement (past dates disabled).
 *  5. Real-time visual feedback (is-valid / is-invalid) with specific contextual error messages.
 */

document.addEventListener('DOMContentLoaded', () => {

  // =========================================================================
  // 1. INPUT RESTRICTION HANDLERS (Letters Only & Numbers Only)
  // =========================================================================

  const navKeys = [
    'Backspace', 'Tab', 'Enter', 'Escape', 'ArrowLeft', 'ArrowRight', 
    'ArrowUp', 'ArrowDown', 'Delete', 'Home', 'End'
  ];

  // Restrict to Letters and Spaces ONLY
  const attachLettersOnly = (input) => {
    if (!input) return;

    input.addEventListener('keydown', (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (navKeys.includes(e.key)) return;

      // Allow only letters (A-Z, a-z) and space
      if (!/^[a-zA-Z\s]$/.test(e.key)) {
        e.preventDefault();
      }
    });

    input.addEventListener('input', (e) => {
      const sanitized = e.target.value.replace(/[^a-zA-Z\s]/g, '');
      if (e.target.value !== sanitized) {
        e.target.value = sanitized;
      }
    });

    input.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData)?.getData('text') || '';
      const sanitized = text.replace(/[^a-zA-Z\s]/g, '');
      try {
        if (!document.execCommand('insertText', false, sanitized)) {
          input.value = sanitized;
          input.dispatchEvent(new Event('input', { bubbles: true }));
        }
      } catch (err) {
        input.value = sanitized;
        input.dispatchEvent(new Event('input', { bubbles: true }));
      }
    });
  };

  // Restrict Location / City fields to letters, spaces, commas, periods, hyphens (No Numbers)
  const attachLocationOnly = (input) => {
    if (!input) return;

    input.addEventListener('keydown', (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (navKeys.includes(e.key)) return;

      // Allow letters, spaces, commas, periods, hyphens
      if (!/^[a-zA-Z\s,.-]$/.test(e.key)) {
        e.preventDefault();
      }
    });

    input.addEventListener('input', (e) => {
      const sanitized = e.target.value.replace(/[^a-zA-Z\s,.-]/g, '');
      if (e.target.value !== sanitized) {
        e.target.value = sanitized;
      }
    });

    input.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData)?.getData('text') || '';
      const sanitized = text.replace(/[^a-zA-Z\s,.-]/g, '');
      try {
        if (!document.execCommand('insertText', false, sanitized)) {
          input.value = sanitized;
          input.dispatchEvent(new Event('input', { bubbles: true }));
        }
      } catch (err) {
        input.value = sanitized;
        input.dispatchEvent(new Event('input', { bubbles: true }));
      }
    });
  };

  // Restrict to Numbers ONLY (Digits 0-9, Max 10 digits)
  const attachNumbersOnly = (input) => {
    if (!input) return;

    input.setAttribute('inputmode', 'numeric');
    input.setAttribute('maxlength', '10');

    input.addEventListener('keydown', (e) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      if (navKeys.includes(e.key)) return;

      // Block non-digits
      if (!/^\d$/.test(e.key)) {
        e.preventDefault();
        return;
      }

      // Block more than 10 digits unless text is highlighted
      if (input.value.length >= 10 && input.selectionStart === input.selectionEnd) {
        e.preventDefault();
      }
    });

    input.addEventListener('input', (e) => {
      const sanitized = e.target.value.replace(/\D/g, '').slice(0, 10);
      if (e.target.value !== sanitized) {
        e.target.value = sanitized;
      }
    });

    input.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData)?.getData('text') || '';
      const sanitized = text.replace(/\D/g, '').slice(0, 10);
      try {
        if (!document.execCommand('insertText', false, sanitized)) {
          input.value = sanitized;
          input.dispatchEvent(new Event('input', { bubbles: true }));
        }
      } catch (err) {
        input.value = sanitized;
        input.dispatchEvent(new Event('input', { bubbles: true }));
      }
    });
  };

  // Restrict Event Date pickers to today or future dates
  const todayISO = new Date().toISOString().split('T')[0];
  document.querySelectorAll('input[type="date"]').forEach(dateInput => {
    dateInput.setAttribute('min', todayISO);
  });

  // Attach global field restrictions
  document.querySelectorAll('input[name="fullName"], input#regName').forEach(attachLettersOnly);
  document.querySelectorAll('input[name="venueCity"], input[name="eventLocation"]').forEach(attachLocationOnly);
  document.querySelectorAll('input[name="phone"], input[type="tel"], input#regPhone').forEach(attachNumbersOnly);

  // =========================================================================
  // 2. VALIDATION UTILITIES & INLINE FEEDBACK
  // =========================================================================

  const setInvalid = (input, message) => {
    if (!input) return false;
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
    let fb = input.parentElement.querySelector('.invalid-feedback');
    if (!fb) {
      fb = document.createElement('div');
      fb.className = 'invalid-feedback';
      input.parentElement.appendChild(fb);
    }
    fb.textContent = message;
    return false;
  };

  const setValid = (input) => {
    if (!input) return true;
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
    const fb = input.parentElement.querySelector('.invalid-feedback');
    if (fb) fb.textContent = '';
    return true;
  };

  const clearValidation = (form) => {
    if (!form) return;
    form.querySelectorAll('.is-invalid, .is-valid').forEach(el => {
      el.classList.remove('is-invalid', 'is-valid');
    });
    form.querySelectorAll('.invalid-feedback').forEach(fb => {
      fb.textContent = '';
    });
  };

  const showFeedback = (alertBox, isSuccess, message) => {
    if (!alertBox) return;
    alertBox.classList.remove('alert-success', 'alert-danger');
    alertBox.classList.add(isSuccess ? 'alert-success' : 'alert-danger');
    alertBox.innerHTML = message;
    alertBox.classList.add('show');
    alertBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  };

  // Specific Validators
  const validateFullName = (input) => {
    const val = input.value.trim();
    if (!val) {
      return setInvalid(input, 'Please enter your full name.');
    }
    if (!/^[a-zA-Z\s]+$/.test(val)) {
      return setInvalid(input, 'Full Name must contain letters only (no numbers or symbols).');
    }
    if (val.replace(/\s/g, '').length < 3) {
      return setInvalid(input, 'Full Name must be at least 3 letters long.');
    }
    return setValid(input);
  };

  const validateEmail = (input) => {
    const val = input.value.trim();
    if (!val) {
      return setInvalid(input, 'Please enter your email address.');
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(val)) {
      return setInvalid(input, 'Please enter a valid email address (e.g. name@example.com).');
    }
    return setValid(input);
  };

  const validatePhone = (input) => {
    const val = input.value.trim();
    if (!val) {
      return setInvalid(input, 'Please enter your 10-digit mobile number.');
    }
    if (!/^\d+$/.test(val)) {
      return setInvalid(input, 'Phone number must contain numbers only.');
    }
    if (val.length !== 10) {
      return setInvalid(input, `Phone number must be exactly 10 digits (currently ${val.length} digits).`);
    }
    if (!/^[6-9]/.test(val)) {
      return setInvalid(input, 'Please enter a valid mobile number starting with 6, 7, 8, or 9.');
    }
    return setValid(input);
  };

  const validateSelect = (select, message) => {
    if (!select.value || select.value === '') {
      return setInvalid(select, message || 'Please select an option from the list.');
    }
    return setValid(select);
  };

  const validateEventDate = (input, isRequired = false) => {
    const val = input.value;
    if (!val) {
      if (isRequired) {
        return setInvalid(input, 'Please select your event date.');
      }
      setValid(input);
      return true;
    }
    const selected = new Date(val);
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    if (selected < today) {
      return setInvalid(input, 'Event date cannot be in the past. Please choose today or a future date.');
    }
    return setValid(input);
  };

  const validateLocation = (input, isRequired = false) => {
    const val = input.value.trim();
    if (!val) {
      if (isRequired) {
        return setInvalid(input, 'Please specify your venue city or area.');
      }
      setValid(input);
      return true;
    }
    if (!/^[a-zA-Z\s,.-]+$/.test(val)) {
      return setInvalid(input, 'Venue location must contain letters only (e.g. MRC Nagar, Chennai).');
    }
    if (val.length < 3) {
      return setInvalid(input, 'Please enter at least 3 letters for the venue area.');
    }
    return setValid(input);
  };

  const validateMessage = (textarea) => {
    const val = textarea.value.trim();
    if (!val) {
      return setInvalid(textarea, 'Please describe your event requirements or inquiries.');
    }
    if (val.length < 10) {
      return setInvalid(textarea, 'Please provide at least 10 characters describing your celebration requirements.');
    }
    return setValid(textarea);
  };

  // =========================================================================
  // 3. CONTACT FORM VALIDATION (#contactForm)
  // =========================================================================

  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    const alertBox = contactForm.querySelector('.feedback-alert');
    const nameInput = contactForm.querySelector('[name="fullName"]');
    const emailInput = contactForm.querySelector('[name="email"]');
    const phoneInput = contactForm.querySelector('[name="phone"]');
    const eventTypeSelect = contactForm.querySelector('[name="eventType"]');
    const dateInput = contactForm.querySelector('[name="eventDate"]');
    const cityInput = contactForm.querySelector('[name="venueCity"]');
    const messageInput = contactForm.querySelector('[name="message"]');

    // Live validation on blur
    if (nameInput) nameInput.addEventListener('blur', () => validateFullName(nameInput));
    if (emailInput) emailInput.addEventListener('blur', () => validateEmail(emailInput));
    if (phoneInput) phoneInput.addEventListener('blur', () => validatePhone(phoneInput));
    if (eventTypeSelect) eventTypeSelect.addEventListener('change', () => validateSelect(eventTypeSelect, 'Please select an event category.'));
    if (dateInput) dateInput.addEventListener('change', () => validateEventDate(dateInput, false));
    if (cityInput) cityInput.addEventListener('blur', () => validateLocation(cityInput, false));
    if (messageInput) messageInput.addEventListener('blur', () => validateMessage(messageInput));

    // Clear error on input if already invalid
    [nameInput, emailInput, phoneInput, cityInput, messageInput].forEach(inp => {
      if (inp) {
        inp.addEventListener('input', () => {
          if (inp.classList.contains('is-invalid')) {
            if (inp === nameInput) validateFullName(nameInput);
            else if (inp === emailInput) validateEmail(emailInput);
            else if (inp === phoneInput) validatePhone(phoneInput);
            else if (inp === cityInput) validateLocation(cityInput, false);
            else if (inp === messageInput) validateMessage(messageInput);
          }
        });
      }
    });

    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const v1 = validateFullName(nameInput);
      const v2 = validateEmail(emailInput);
      const v3 = validatePhone(phoneInput);
      const v4 = validateSelect(eventTypeSelect, 'Please select an event category.');
      const v5 = dateInput ? validateEventDate(dateInput, false) : true;
      const v6 = cityInput ? validateLocation(cityInput, false) : true;
      const v7 = validateMessage(messageInput);

      if (!v1 || !v2 || !v3 || !v4 || !v5 || !v6 || !v7) {
        showFeedback(
          alertBox,
          false,
          '<i class="bi bi-exclamation-triangle-fill me-2"></i><strong>Validation Error:</strong> Please fix the highlighted fields below. Letters only for Name, numbers only for Phone.'
        );
        const firstInvalid = contactForm.querySelector('.is-invalid');
        if (firstInvalid) {
          firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstInvalid.focus();
        }
        return;
      }

      // Success
      const clientName = nameInput.value.trim();
      showFeedback(
        alertBox,
        true,
        `<i class="bi bi-check-circle-fill me-2"></i><strong>Thank you, ${clientName}!</strong> Your event inquiry has been received. Our senior event architect will contact you on <strong>${phoneInput.value.trim()}</strong> within 24 hours.`
      );
      contactForm.reset();
      clearValidation(contactForm);
    });
  }

  // =========================================================================
  // 4. GET A QUOTE FORM VALIDATION (#quoteForm)
  // =========================================================================

  const quoteForm = document.getElementById('quoteForm');
  if (quoteForm) {
    const alertBox = quoteForm.querySelector('.feedback-alert');
    const nameInput = quoteForm.querySelector('[name="fullName"]');
    const emailInput = quoteForm.querySelector('[name="email"]');
    const phoneInput = quoteForm.querySelector('[name="phone"]');
    const eventTypeSelect = quoteForm.querySelector('[name="eventType"]');
    const dateInput = quoteForm.querySelector('[name="eventDate"]');
    const locationInput = quoteForm.querySelector('[name="eventLocation"]');

    if (nameInput) nameInput.addEventListener('blur', () => validateFullName(nameInput));
    if (emailInput) emailInput.addEventListener('blur', () => validateEmail(emailInput));
    if (phoneInput) phoneInput.addEventListener('blur', () => validatePhone(phoneInput));
    if (eventTypeSelect) eventTypeSelect.addEventListener('change', () => validateSelect(eventTypeSelect, 'Please select an event category.'));
    if (dateInput) dateInput.addEventListener('change', () => validateEventDate(dateInput, true));
    if (locationInput) locationInput.addEventListener('blur', () => validateLocation(locationInput, true));

    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const v1 = validateFullName(nameInput);
      const v2 = validateEmail(emailInput);
      const v3 = validatePhone(phoneInput);
      const v4 = validateSelect(eventTypeSelect, 'Please select an event category.');
      const v5 = validateEventDate(dateInput, true);
      const v6 = validateLocation(locationInput, true);

      if (!v1 || !v2 || !v3 || !v4 || !v5 || !v6) {
        showFeedback(
          alertBox,
          false,
          '<i class="bi bi-exclamation-triangle-fill me-2"></i><strong>Please complete all required fields correctly:</strong> Letters only for Name/Location, 10-digit numbers only for Phone.'
        );
        const firstInvalid = quoteForm.querySelector('.is-invalid');
        if (firstInvalid) {
          firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstInvalid.focus();
        }
        return;
      }

      const clientName = nameInput.value.trim();
      showFeedback(
        alertBox,
        true,
        `<i class="bi bi-check-circle-fill me-2"></i><strong>Quote Request Confirmed!</strong> Thank you, ${clientName}. Our engineering & decor team is preparing custom 3D estimates for your event.`
      );
      quoteForm.reset();
      clearValidation(quoteForm);
    });
  }

  // =========================================================================
  // 5. REGISTER FORM VALIDATION (#registerForm)
  // =========================================================================

  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    const alertBox = registerForm.querySelector('.feedback-alert');
    const nameInput = registerForm.querySelector('[name="fullName"]');
    const phoneInput = registerForm.querySelector('[name="phone"]');
    const emailInput = registerForm.querySelector('[name="email"]');
    const roleSelect = registerForm.querySelector('[name="role"]');
    const dateInput = registerForm.querySelector('[name="eventDate"]');
    const passInput = registerForm.querySelector('[name="password"]');
    const confirmInput = registerForm.querySelector('[name="confirmPassword"]');
    const termsCheck = registerForm.querySelector('[name="terms"]');

    if (nameInput) nameInput.addEventListener('blur', () => validateFullName(nameInput));
    if (phoneInput) phoneInput.addEventListener('blur', () => validatePhone(phoneInput));
    if (emailInput) emailInput.addEventListener('blur', () => validateEmail(emailInput));
    if (roleSelect) roleSelect.addEventListener('change', () => validateSelect(roleSelect, 'Please select your role.'));
    if (dateInput) dateInput.addEventListener('change', () => validateEventDate(dateInput, false));

    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const v1 = validateFullName(nameInput);
      const v2 = validatePhone(phoneInput);
      const v3 = validateEmail(emailInput);
      const v4 = validateSelect(roleSelect, 'Please select your role.');
      const v5 = dateInput ? validateEventDate(dateInput, false) : true;

      let vPass = true;
      if (!passInput.value || passInput.value.length < 8) {
        vPass = setInvalid(passInput, 'Password must be at least 8 characters.');
      } else {
        setValid(passInput);
      }

      let vConfirm = true;
      if (!confirmInput.value || confirmInput.value !== passInput.value) {
        vConfirm = setInvalid(confirmInput, 'Passwords do not match.');
      } else {
        setValid(confirmInput);
      }

      let vTerms = true;
      if (termsCheck && !termsCheck.checked) {
        termsCheck.classList.add('is-invalid');
        vTerms = false;
      } else if (termsCheck) {
        termsCheck.classList.remove('is-invalid');
      }

      if (!v1 || !v2 || !v3 || !v4 || !v5 || !vPass || !vConfirm || !vTerms) {
        showFeedback(
          alertBox,
          false,
          '<i class="bi bi-exclamation-triangle-fill me-2"></i>Please fill out all registration fields correctly.'
        );
        const firstInvalid = registerForm.querySelector('.is-invalid');
        if (firstInvalid) {
          firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
          firstInvalid.focus();
        }
        return;
      }

      showFeedback(
        alertBox,
        true,
        '<i class="bi bi-check-circle-fill me-2"></i><strong>Account Created!</strong> Welcome to UTSAV Client Portal. You can now access 3D blueprints and quotes.'
      );
      registerForm.reset();
      clearValidation(registerForm);
    });
  }

});
