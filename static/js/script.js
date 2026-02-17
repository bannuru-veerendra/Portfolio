/**
 * Portfolio Website Scripts
 * Main JavaScript file for the portfolio website.
 * Handles navigation, animations, and interactive features.
 */

// DOM Elements
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('nav-menu');

// Navigation Functionality

/**
 * Navigation scroll effect - Adds background blur when scrolling.
 * Updates active navigation link based on current section.
 */
window.addEventListener('scroll', () => {
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }

    // Update active nav link
    updateActiveNavLink();
});

/**
 * Updates the active navigation link based on current scroll position
 * Highlights the navigation item corresponding to the visible section
 */
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section');
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (sectionId && scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

/**
 * Smooth scrolling for navigation links.
 * Closes mobile menu after navigation.
 */
const NAVBAR_OFFSET = 70;

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
            const offsetTop = targetSection.offsetTop - NAVBAR_OFFSET;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }

        // Close mobile menu if open
        if (navMenu && hamburger) {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });
});

/**
 * Mobile menu: hamburger toggle and keyboard (Escape) close.
 */
if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        const isExpanded = hamburger.classList.contains('active');
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', String(!isExpanded));
    });

    // Close menu on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
            hamburger.setAttribute('aria-expanded', 'false');
        }
    });
}

// Scroll Animations
const ANIMATION_OBSERVER_OPTIONS = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const animationObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, ANIMATION_OBSERVER_OPTIONS);

// Observe all animatable elements
const animatableSelectors = [
    '.project-card',
    '.certification-card',
    '.experience-item',
    '.education-item',
    '.skill-category'
];

animatableSelectors.forEach(selector => {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => animationObserver.observe(element));
});

/**
 * API Functions
 * Fetch portfolio data from backend API and render dynamically
 */

/**
 * Fetch data from API endpoint
 */
async function fetchAPI(endpoint) {
    try {
        const response = await fetch(`/api/${endpoint}`);
        const data = await response.json();
        if (data.success) {
            return data.data;
        }
        throw new Error(data.message || 'Failed to fetch data');
    } catch (error) {
        console.error(`Error fetching ${endpoint}:`, error);
        return null;
    }
}

/**
 * Render projects dynamically
 */
async function renderProjects() {
    const projects = await fetchAPI('projects');
    if (!projects) return;

    const projectsGrid = document.querySelector('.projects-grid');
    if (!projectsGrid) return;

    projectsGrid.innerHTML = projects.map(project => {
        const linksHTML = project.links.map(link => {
            const iconClass = link.type === 'live' ? 'fas fa-external-link-alt' : 'fab fa-github';
            const ariaLabel = link.type === 'live' ? 'View Project' : 'View Code';
            return `<a href="${link.url}" target="_blank" rel="noopener noreferrer" class="project-link" aria-label="${ariaLabel}">
                <i class="${iconClass}"></i>
            </a>`;
        }).join('');

        const tagsHTML = project.tags.map(tag => `<span class="tag">${tag}</span>`).join('');

        return `
            <div class="project-card">
                <div class="project-image">
                    <div class="project-placeholder">
                        <i class="${project.icon}"></i>
                    </div>
                </div>
                <div class="project-content">
                    <div class="project-header">
                        <h3 class="project-title">${project.title}</h3>
                        <div class="project-links">${linksHTML}</div>
                    </div>
                    <p class="project-description">${project.description}</p>
                    <div class="project-tags">${tagsHTML}</div>
                </div>
            </div>
        `;
    }).join('');

    // Re-observe new project cards for animations
    document.querySelectorAll('.project-card').forEach(card => {
        animationObserver.observe(card);
    });
}

/**
 * Render skills dynamically
 */
async function renderSkills() {
    const skillsGrid = document.querySelector('.skills-grid');
    if (!skillsGrid) return;

    const skills = await fetchAPI('skills');
    if (!skills || skills.length === 0) {
        skillsGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Unable to load skills. Please refresh the page.</p>';
        return;
    }

    skillsGrid.innerHTML = skills.map(category => {
        const skillsHTML = category.skills.map(skill => `<span class="skill-tag">${skill}</span>`).join('');
        return `
            <div class="skill-category">
                <h3 class="category-title">${category.title}</h3>
                <div class="skill-tags">${skillsHTML}</div>
            </div>
        `;
    }).join('');

    // Re-observe new skill categories for animations
    document.querySelectorAll('.skill-category').forEach(category => {
        animationObserver.observe(category);
    });
}

/**
 * Render experience dynamically
 */
async function renderExperience() {
    const experience = await fetchAPI('experience');
    if (!experience) return;

    const experienceTimeline = document.querySelector('.experience-timeline');
    if (!experienceTimeline) return;

    experienceTimeline.innerHTML = experience.map(exp => {
        const descriptionHTML = exp.description.map(desc => `<li>${desc}</li>`).join('');
        const tagsHTML = exp.tags.map(tag => `<span class="experience-tag">${tag}</span>`).join('');

        return `
            <div class="experience-item">
                <div class="experience-dot"></div>
                <div class="experience-content">
                    <div class="experience-period">${exp.period}</div>
                    <h3 class="experience-title">${exp.title}</h3>
                    <div class="experience-company">${exp.company} – ${exp.location}</div>
                    <ul class="experience-description">${descriptionHTML}</ul>
                    <div class="experience-tags">${tagsHTML}</div>
                </div>
            </div>
        `;
    }).join('');

    // Re-observe new experience items for animations
    document.querySelectorAll('.experience-item').forEach(item => {
        animationObserver.observe(item);
    });
}

/**
 * Render education dynamically
 */
async function renderEducation() {
    const educationTimeline = document.querySelector('.education-timeline');
    if (!educationTimeline) return;

    const education = await fetchAPI('education');
    if (!education || education.length === 0) {
        educationTimeline.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Unable to load education. Please refresh the page.</p>';
        return;
    }

    educationTimeline.innerHTML = education.map(edu => `
        <div class="education-item">
            <div class="education-dot"></div>
            <div class="education-content">
                <div class="education-period">${edu.period}</div>
                <h3 class="education-title">${edu.title}</h3>
                <div class="education-institution">${edu.institution}</div>
                <div class="education-location">${edu.location}</div>
                <div class="education-grade">${edu.grade}</div>
            </div>
        </div>
    `).join('');

    // Re-observe new education items for animations
    document.querySelectorAll('.education-item').forEach(item => {
        animationObserver.observe(item);
    });
}

/**
 * Render certifications dynamically
 */
async function renderCertifications() {
    const certificationsGrid = document.querySelector('.certifications-grid');
    if (!certificationsGrid) return;

    const certifications = await fetchAPI('certifications');
    if (!certifications || certifications.length === 0) {
        certificationsGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Unable to load certifications. Please refresh the page.</p>';
        return;
    }

    certificationsGrid.innerHTML = certifications.map(cert => `
        <div class="certification-card">
            <div class="certification-icon">
                <i class="${cert.icon}"></i>
            </div>
            <h3 class="certification-title">${cert.title}</h3>
            <div class="certification-issuer">${cert.issuer}</div>
            <div class="certification-description">${cert.description}</div>
        </div>
    `).join('');

    // Re-observe new certification cards for animations
    document.querySelectorAll('.certification-card').forEach(card => {
        animationObserver.observe(card);
    });
}

/**
 * Update statistics from API
 */
async function updateStats() {
    const stats = await fetchAPI('stats');
    if (!stats) return;

    const statElements = {
        'github_projects': document.querySelector('.stat-item:nth-child(1) .stat-number'),
        'live_projects': document.querySelector('.stat-item:nth-child(2) .stat-number'),
        'years_experience': document.querySelector('.stat-item:nth-child(3) .stat-number')
    };

    if (statElements.github_projects) {
        statElements.github_projects.textContent = stats.github_projects;
    }
    if (statElements.live_projects) {
        statElements.live_projects.textContent = stats.live_projects;
    }
    if (statElements.years_experience) {
        statElements.years_experience.textContent = stats.years_experience;
    }
}

// Contact form: AJAX submit, show success/error on same page
function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;
    const statusEl = document.getElementById('form-status');
    const submitBtn = document.getElementById('submit-btn');
    const submitText = document.getElementById('submit-text');
    const submitIcon = document.getElementById('submit-icon');

    const setStatus = (msg, ok) => {
        if (!statusEl) return;
        statusEl.textContent = msg || '';
        statusEl.classList.toggle('is-success', ok === true);
        statusEl.classList.toggle('is-error', ok === false);
        statusEl.setAttribute('aria-hidden', msg ? 'false' : 'true');
    };

    const setBusy = (busy) => {
        if (submitBtn) submitBtn.disabled = busy;
        if (submitText) submitText.textContent = busy ? 'Sending...' : 'Send Message';
        if (submitIcon) submitIcon.className = busy ? 'fas fa-spinner fa-spin' : 'fas fa-paper-plane';
    };

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        setStatus('', null);
        setBusy(true);
        try {
            const res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'X-Requested-With': 'XMLHttpRequest' } });
            const data = await res.json().catch(() => ({}));
            const ok = Boolean(res.ok && data.success);
            setStatus(data.message || (ok ? "Message sent successfully! I'll get back to you soon." : 'Something went wrong. Please try again or email me directly.'), ok);
            if (ok) form.reset();
        } catch {
            setStatus('Network error. Please try again or email me directly.', false);
        } finally {
            setBusy(false);
        }
    });
}

// Page Initialization
document.addEventListener('DOMContentLoaded', async () => {
    // Set initial active nav link
    updateActiveNavLink();
    initContactForm();

    // Load data from API
    await Promise.all([
        renderProjects(),
        renderSkills(),
        renderExperience(),
        renderEducation(),
        renderCertifications(),
        updateStats()
    ]);
});
