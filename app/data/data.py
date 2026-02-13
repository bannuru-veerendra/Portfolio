"""
Portfolio Data
Portfolio data definitions and retrieval functions
"""

from typing import List, Dict, Any
from app.models.models import (
    Project, ProjectLink, SkillCategory, ExperienceItem,
    EducationItem, Certification, PortfolioStats
)
from app.models.serializers import Serializers


class Data:
    """Portfolio data access and retrieval"""

    @staticmethod
    def get_projects() -> List[Dict[str, Any]]:
        """
        Get all projects

        Returns:
            List of project dictionaries
        """
        projects = [
            Project(
                title="AccessVault",
                description=(
                    "Enterprise-grade backend API system for user management and authentication. Built with Flask "
                    "and PostgreSQL, featuring secure JWT-based authentication with token rotation, password hashing "
                    "(bcrypt), and role-based access control. Implemented comprehensive admin APIs for user management, "
                    "audit logging, and system monitoring. Added rate limiting, API documentation with Swagger, and "
                    "production-ready error handling. Deployed on cloud infrastructure with high availability."
                ),
                tags=["Flask", "Python", "PostgreSQL", "JWT", "Redis", "Swagger", "Render"],
                links=[
                    ProjectLink(type="live", url="https://accessvault-api-8shv.onrender.com/", label="View Project"),
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/AccessVault", label="View Code")
                ],
                icon="fas fa-shield-alt"
            ),
            Project(
                title="DevShare",
                description=(
                    "Full-stack web application built with ReactJS frontend and Flask/Python backend. "
                    "Architected scalable RESTful API endpoints for user authentication, project management, "
                    "and social features. Implemented real-time data synchronization, optimized database queries, "
                    "and deployed on cloud infrastructure. Designed secure authentication system with JWT tokens "
                    "and role-based access control."
                ),
                tags=["ReactJS", "Flask", "TypeScript", "Python", "REST APIs", "MongoDB"],
                links=[
                    ProjectLink(type="live", url="https://devshare-68.web.app/", label="View Project"),
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/DevShare", label="View Code")
                ],
                icon="fas fa-laptop-code"
            ),
            Project(
                title="SecurePay Fraud Detection",
                description=(
                    "Machine Learning-powered fraud detection system built with Python. Developed backend services "
                    "that process financial transactions in real-time, implementing ensemble ML models for "
                    "high-accuracy fraud detection. Built RESTful APIs for transaction processing, integrated with "
                    "database systems for pattern analysis, and created monitoring dashboards. Designed scalable "
                    "architecture to handle high-volume transaction processing."
                ),
                tags=["Python", "Machine Learning", "TensorFlow", "scikit-learn"],
                links=[
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/SecurePay-Fraud-Detection", label="View Code")
                ],
                icon="fas fa-shield-alt"
            ),
            Project(
                title="Music Hub",
                description=(
                    "Full-stack music streaming platform built with Java Spring Boot backend and MySQL database. "
                    "Architected RESTful APIs for user management, playlist operations, and media metadata. "
                    "Integrated Razorpay payment gateway APIs for subscription management. Implemented secure "
                    "authentication, role-based access control, and optimized database queries for high-performance "
                    "media catalog operations. Designed scalable backend architecture to handle concurrent user requests."
                ),
                tags=["Java", "Spring Boot", "MySQL", "Razorpay"],
                links=[
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/Music-Hub", label="View Code")
                ],
                icon="fas fa-music"
            ),
            Project(
                title="HRMS Logging System",
                description=(
                    "Enterprise microservices architecture built with Java Spring Boot. Designed and implemented "
                    "multiple backend services with RESTful APIs, integrated distributed tracing using Zipkin, and "
                    "implemented service discovery patterns. Built API gateway for request routing, implemented "
                    "circuit breakers for fault tolerance, and set up centralized logging and monitoring systems. "
                    "Designed scalable microservices architecture following best practices."
                ),
                tags=["Java", "Spring Boot", "Zipkin", "Dynatrace"],
                links=[
                    ProjectLink(type="github", url="https://github.com/suniljeevan/Presi-HRMS/tree/master", label="View Code")
                ],
                icon="fas fa-building"
            ),
            Project(
                title="GuessMaster-2025",
                description=(
                    "An interactive, full-stack web-based number guessing game that combines strategy and competition "
                    "with real-time score tracking. It offers both single-player and multiplayer modes, where players "
                    "are challenged to guess a randomly generated number within a limited number of attempts. Features "
                    "efficient error handling, logging, and a sleek, responsive user interface. High scores are stored "
                    "for both modes, allowing players to compete for the top spot."
                ),
                tags=["Python", "Flask", "JavaScript", "Bootstrap"],
                links=[
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/GuessMaster-2025", label="View Code")
                ],
                icon="fas fa-gamepad"
            )
        ]

        return [Serializers.project_to_dict(p) for p in projects]

    @staticmethod
    def get_skills() -> List[Dict[str, Any]]:
        """
        Get all skills organized by category

        Returns:
            List of skill category dictionaries
        """
        categories = [
            SkillCategory(
                title="Programming & Frameworks",
                skills=["Python", "Flask", "FastAPI", "JavaScript"]
            ),
            SkillCategory(
                title="Backend & Architecture",
                skills=["REST APIs", "Microservices", "OOP", "JWT Authentication", "API Security", "RabbitMQ"]
            ),
            SkillCategory(
                title="Databases & ORM",
                skills=["PostgreSQL", "MySQL", "MongoDB", "Supabase", "SQLAlchemy", "Redis"]
            ),
            SkillCategory(
                title="Data Science & ML",
                skills=["NumPy", "Pandas", "scikit-learn", "Matplotlib", "Seaborn"]
            ),
            SkillCategory(
                title="DevOps & Tools",
                skills=["Docker", "Git", "GitHub", "Postman", "Render", "CI/CD", "Linux", "VS Code", "Cursor AI"]
            ),
            SkillCategory(
                title="Frontend Technologies",
                skills=["HTML", "CSS", "JavaScript", "React.js"]
            )
        ]

        return [Serializers.skill_category_to_dict(c) for c in categories]

    @staticmethod
    def get_experience() -> List[Dict[str, Any]]:
        """
        Get all experience items

        Returns:
            List of experience item dictionaries
        """
        experience = [
            ExperienceItem(
                period="Aug 2024 - Present",
                title="Backend Software Engineer",
                company="Por's and Rao's Studio",
                location="Bengaluru, India",
                description=[
                    "Worked independently with full ownership of projects from design and implementation through deployment and maintenance",
                    "Maintained an internal Python library used across the team, ensuring code quality, stability, and ease of integration",
                    "Designed and implemented a new REST API within the library to expose core capabilities for internal and external consumers",
                    "Added new features and functionality to the existing library to support evolving project and product requirements",
                    "Built a head detection model from dataset creation through training for use in downstream applications",
                    "Used Docker Desktop for containerized development environments and RabbitMQ for message-based pipeline integration",
                    "Used Git and GitHub for version control, code updates, and collaborative development workflows",
                    "Authored comprehensive technical documentation including API specs, architecture notes, and usage guides for the library",
                    "Leveraged Cursor AI to speed up development, improve code quality, and deliver features more efficiently"
                ],
                tags=["Python", "Flask", "REST API", "Backend Development", "API Development", "Git", "GitHub", "Docker", "RabbitMQ", "Technical Documentation", "Cursor AI"]
            )
        ]

        return [Serializers.experience_to_dict(e) for e in experience]

    @staticmethod
    def get_education() -> List[Dict[str, Any]]:
        """
        Get all education items

        Returns:
            List of education item dictionaries
        """
        education = [
            EducationItem(
                period="2019 – 2023",
                title="B.Tech in Information Science and Technology",
                institution="Presidency University",
                location="Bengaluru, India",
                grade="CGPA: 8.21"
            ),
            EducationItem(
                period="2017 – 2019",
                title="Higher Secondary (Grade 12, MPC)",
                institution="Narayana Junior College",
                location="Andhra Pradesh, India",
                grade="CGPA: 9.03"
            ),
            EducationItem(
                period="2017",
                title="Secondary Education (Grade 10)",
                institution="Good Shepherd English Medium School",
                location="Andhra Pradesh, India",
                grade="CGPA: 9.00"
            )
        ]

        return [Serializers.education_to_dict(e) for e in education]

    @staticmethod
    def get_certifications() -> List[Dict[str, Any]]:
        """
        Get all certifications

        Returns:
            List of certification dictionaries
        """
        certifications = [
            Certification(
                title="Rest API",
                issuer="HackerRank",
                description="REST API (2025)",
                icon="fas fa-plug"
            ),
            Certification(
                title="Python",
                issuer="HackerRank",
                description="Python (2022)",
                icon="fab fa-python"
            ),
            Certification(
                title="Python Developer",
                issuer="Sololearn",
                description="Python Programming",
                icon="fab fa-python"
            ),
            Certification(
                title="Full Stack Development Training",
                issuer="Kodnest",
                description="Full Stack Web Development",
                icon="fas fa-code"
            ),
            Certification(
                title="Machine Learning Course",
                issuer="Unschool",
                description="Machine Learning Python",
                icon="fas fa-brain"
            ),
            Certification(
                title="HTML, JavaScript, & Bootstrap",
                issuer="Udemy",
                description="HTML5 JavaScript Bootstrap",
                icon="fab fa-html5"
            ),
            Certification(
                title="Java Developer",
                issuer="Sololearn",
                description="Java Programming",
                icon="fab fa-java"
            ),
            Certification(
                title="National Conference Paper Presentation",
                issuer="National Conference",
                description="Research Technical Presentation (2023)",
                icon="fas fa-graduation-cap"
            )
        ]

        return [Serializers.certification_to_dict(c) for c in certifications]

    @staticmethod
    def get_stats() -> Dict[str, Any]:
        """
        Get portfolio statistics

        Returns:
            Dictionary with portfolio statistics
        """
        stats = PortfolioStats(
            github_projects=14,
            live_projects=2,
            years_experience=1.6
        )

        return Serializers.stats_to_dict(stats)