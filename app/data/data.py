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
                    "Enterprise auth API with JWT, RBAC, rate limiting, and Swagger docs. "
                    "Health checks, admin APIs, and structured error handling on Render."
                ),
                tags=["Flask", "PostgreSQL", "Redis", "JWT", "RBAC", "Swagger", "Render"],
                links=[
                    ProjectLink(type="live", url="https://accessvault-api-8shv.onrender.com/api/swagger-ui/", label="Swagger UI"),
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/access-vault", label="View Code")
                ],
                icon="fas fa-shield-alt",
                featured=True,
                image="images/projects/accessvault.png"
            ),
            Project(
                title="RideCare",
                description=(
                    "Vehicle companion for fuel logs, service history, and analytics. "
                    "FastAPI backend with React frontend, Alembic migrations, and GitHub Actions CI."
                ),
                tags=["FastAPI", "React", "PostgreSQL", "Redis", "SQLAlchemy", "JWT", "Alembic", "GitHub Actions"],
                links=[
                    ProjectLink(type="live", url="https://ride-care-jade.vercel.app/", label="Live App"),
                    ProjectLink(type="docs", url="https://ride-care.onrender.com/docs", label="API Docs"),
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/ride-care", label="View Code")
                ],
                icon="fas fa-car",
                featured=True,
                image="images/projects/ridecare.png"
            ),
            Project(
                title="DevShare",
                description=(
                    "Developer social platform with project showcases, posts, and feeds. "
                    "React frontend with Firebase auth and hosting."
                ),
                tags=["React", "Firebase", "JavaScript", "REST APIs"],
                links=[
                    ProjectLink(type="live", url="https://devshare-68.web.app/", label="View Project"),
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/dev-share", label="View Code")
                ],
                icon="fas fa-laptop-code",
                featured=True,
                image="images/projects/devshare.png"
            ),
            Project(
                title="AccessVault FastAPI",
                description=(
                    "Async FastAPI rewrite of AccessVault with the same JWT auth and RBAC model, "
                    "SQLAlchemy 2.0, and auto-generated OpenAPI docs."
                ),
                tags=["FastAPI", "PostgreSQL", "Redis", "JWT", "SQLAlchemy", "OpenAPI"],
                links=[
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/access-vault-fastapi", label="View Code")
                ],
                icon="fas fa-bolt"
            ),
            Project(
                title="SecurePay Fraud Detection",
                description=(
                    "REST API for real-time transaction fraud scoring with scikit-learn."
                ),
                tags=["Python", "Machine Learning", "REST APIs"],
                links=[
                    ProjectLink(type="github", url="https://github.com/bannuru-veerendra/secure-pay-fraud-detection", label="View Code")
                ],
                icon="fas fa-chart-line"
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
                title="Core Stack",
                skills=["Python", "Flask", "FastAPI", "PostgreSQL", "Redis", "SQLAlchemy"]
            ),
            SkillCategory(
                title="Backend Engineering",
                skills=[
                    "REST APIs", "JWT & RBAC", "Rate Limiting", "OpenAPI/Swagger",
                    "Testing", "RabbitMQ", "Alembic", "API Security"
                ]
            ),
            SkillCategory(
                title="DevOps & Deployment",
                skills=["Docker", "GitHub Actions", "CI/CD", "Render", "Vercel", "Gunicorn", "Linux"]
            ),
            SkillCategory(
                title="Also Experienced With",
                skills=["React", "JavaScript", "Firebase", "MongoDB", "YOLO/ML", "Pandas", "scikit-learn"]
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
                period="Aug 2024 – Present",
                title="Junior Software Engineer",
                company="Pors & Rao",
                location="Bengaluru, India",
                description=[
                    "Developed and maintained 40+ REST APIs in an internal library used across multiple production projects",
                    "Optimized PostgreSQL query performance, measurably improving endpoint response times",
                    "Built a computer vision pipeline for human head detection using YOLOv11 — model integration, inference optimization, and deployment",
                    "Wrote unit and integration tests for backend features running in production",
                    "Built 2 backend features from scratch, improving code reusability and reducing duplication",
                    "Integrated RabbitMQ for real-time service communication across microservices",
                    "Refactored legacy codebases and shipped new functionality in Agile sprints"
                ],
                tags=["YOLOv11", "RabbitMQ", "Internal Library", "ML Workflow"]
            ),
            ExperienceItem(
                period="Apr 2024 – Jul 2024",
                title="Software Engineering Intern",
                company="Deepnet Labs",
                location="Bengaluru, India",
                description=[
                    "Worked with internal Python libraries and development workflows",
                    "Learned framework integration and configurable system architecture",
                    "Prepared technical documentation for internal systems"
                ],
                tags=["Internal Libraries", "System Architecture"]
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
                grade="CGPA: 8.21/10"
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
                icon="fas fa-plug",
                url="https://www.hackerrank.com/certificates/iframe/023ce60b561f"
            ),
            Certification(
                title="Python",
                issuer="HackerRank",
                description="Python (2022)",
                icon="fab fa-python",
                url="https://www.hackerrank.com/certificates/iframe/274384521e95"
            ),
            Certification(
                title="SQL",
                issuer="Udemy",
                description="SQL Programming",
                icon="fas fa-database",
                url="https://www.udemy.com/certificate/UC-c3330878-9411-4951-b71c-551a0cc36308/"
            ),
            Certification(
                title="Python Developer",
                issuer="Sololearn",
                description="Python Programming",
                icon="fab fa-python",
                url="https://www.sololearn.com/en/certificates/CC-E5ZYG7VL"
            ),
            Certification(
                title="Java Developer",
                issuer="Sololearn",
                description="Java Programming",
                icon="fab fa-java",
                url="https://www.sololearn.com/en/certificates/CT-FOZBJAUK"
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
            live_projects=3,
            years_experience="2+",
        )

        return Serializers.stats_to_dict(stats)
