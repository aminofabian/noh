from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

python_posts = [
  {
    "id": 1,
    "title": "Getting Started with Python: Installation and Setup",
    "content": "Learn how to download and install Python on your system. Set up your development environment with IDEs like PyCharm, VS Code, or Jupyter Notebook. Understand basic syntax and run your first 'Hello, World!' program."
  },
  {
    "id": 2,
    "title": "Python Basics: Variables, Data Types, and Operators",
    "content": "Explore fundamental concepts like variables, strings, integers, floats, and booleans. Master basic operators such as arithmetic, comparison, and logical operators. Understand how to manipulate data efficiently."
  },
  {
    "id": 3,
    "title": "Control Flow: Conditional Statements and Loops",
    "content": "Master the use of conditional statements (if, elif, else) and loops (for and while). Learn how to use break, continue, and else within loops to control the flow of your programs."
  },
  {
    "id": 4,
    "title": "Data Structures: Lists, Tuples, Sets, and Dictionaries",
    "content": "Dive into Python's core data structures: lists for ordered collections, tuples for immutable sequences, sets for unique items, and dictionaries for key-value pairs. Learn how to manipulate and iterate through each."
  },
  {
    "id": 5,
    "title": "Functions and Modules: Reusable Code",
    "content": "Write reusable and modular code with functions. Learn how to define functions, pass arguments, and return values. Explore built-in modules and learn how to import and use them in your projects."
  },
  {
    "id": 6,
    "title": "Object-Oriented Programming (OOP) in Python",
    "content": "Understand the principles of OOP, including classes, objects, inheritance, polymorphism, encapsulation, and abstraction. Learn how to create and use custom classes effectively."
  },
  {
    "id": 7,
    "title": "Working with Files and Directories",
    "content": "Learn how to read from and write to files using Python. Explore file handling techniques, including opening, reading, writing, and closing files safely. Understand how to manipulate directories with the os module."
  },
  {
    "id": 8,
    "title": "Error Handling and Debugging",
    "content": "Handle errors gracefully using try, except, finally, and raise. Learn how to debug your code using print statements and debugging tools. Understand common errors and how to resolve them."
  },
  {
    "id": 9,
    "title": "Python Libraries and Frameworks: Exploring the Ecosystem",
    "content": "Get familiar with popular libraries like NumPy, Pandas, Matplotlib, and frameworks like Django and Flask. Understand how to install packages using pip and manage dependencies."
  },
  {
    "id": 10,
    "title": "Building Real-World Projects with Python",
    "content": "Consolidate your learning by building projects like a web scraper, a basic API, or a data visualization dashboard. Learn the best practices for project structure, version control, and deployment."
  }
]

django_posts = [
  {
    "id": 1,
    "title": "Introduction to Django: What and Why",
    "content": "Discover what Django is and why it's a popular choice for web development. Learn about Django's core features, including its robust ORM, built-in admin interface, and rapid development capabilities."
  },
  {
    "id": 2,
    "title": "Setting Up Your Django Environment",
    "content": "Learn how to install Django using pip, set up a virtual environment, and create your first Django project. Understand the structure of a Django project and the purpose of each folder and file."
  },
  {
    "id": 3,
    "title": "Creating Your First Django App",
    "content": "Learn how to create a new app within your Django project. Understand the concept of apps in Django, how to register them, and how to set up URLs and views to display a simple page."
  },
  {
    "id": 4,
    "title": "Django Models: Designing Your Database",
    "content": "Explore how to define models in Django, including fields, relationships, and methods. Learn how to make migrations and apply them to create database tables automatically."
  },
  {
    "id": 5,
    "title": "Views and Templates: Displaying Data",
    "content": "Learn how to create views that handle HTTP requests and return responses. Use templates to render HTML content dynamically, and explore template inheritance for maintaining a consistent layout."
  },
  {
    "id": 6,
    "title": "Forms and User Input",
    "content": "Handle user input using Django forms. Learn how to create forms, validate input, and process form data. Explore model forms for automatic form generation from your models."
  },
  {
    "id": 7,
    "title": "Django Admin: Managing Your Application",
    "content": "Leverage the built-in Django admin interface to manage your database records. Customize the admin dashboard to display your models and make it more intuitive for administrators."
  },
  {
    "id": 8,
    "title": "Authentication and Authorization",
    "content": "Implement user authentication using Django's built-in system. Learn how to register users, handle login and logout, and restrict access to certain pages using authentication decorators."
  },
  {
    "id": 9,
    "title": "Building RESTful APIs with Django and Django REST Framework",
    "content": "Create APIs using Django REST Framework (DRF). Learn how to serialize data, create API views, and implement CRUD operations. Explore API authentication using tokens or JWT."
  },
  {
    "id": 10,
    "title": "Deployment: Taking Your Django Project Live",
    "content": "Learn how to deploy your Django project to production using platforms like Heroku, DigitalOcean, or AWS. Configure settings for production, including static files, security, and database settings."
  }
]

def get_nav_html():
    nav_style = """
        <style>
            body {
                margin: 0;
                padding: 0;
                min-height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }
            .header {
                background-color: #4CAF50;
                padding: 15px 0;
                position: sticky;
                top: 0;
                z-index: 1000;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .nav-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            .logo {
                color: white;
                font-size: 1.5em;
                text-decoration: none;
                font-weight: bold;
            }
            .nav-links {
                display: flex;
                gap: 20px;
            }
            .nav-button {
                color: white;
                text-decoration: none;
                padding: 8px 16px;
                border-radius: 5px;
                transition: background-color 0.3s ease;
            }
            .nav-button:hover {
                background-color: #45a049;
            }
            .content {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
                text-align: center;
            }
            p {
                line-height: 1.6;
                color: #666;
            }
            .app-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 20px;
                max-width: 600px;
                margin: 40px auto;
                padding: 20px;
            }
            .app-button {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                background-color: white;
                border-radius: 15px;
                padding: 20px;
                text-decoration: none;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s, box-shadow 0.2s;
                aspect-ratio: 1;
            }
            .app-button:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }
            .app-icon {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .app-label {
                color: #333;
                font-weight: bold;
                text-align: center;
            }
            .about-container {
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background-color: white;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .profile-section {
                text-align: center;
                margin-bottom: 30px;
            }
            .tech-stack {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin: 20px 0;
            }
            .tech-badge {
                background-color: #3498db;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
            }
            .learning-badge {
                background-color: #2ecc71;
            }
            .projects-section {
                margin: 30px 0;
            }
            .project-category {
                margin-bottom: 30px;
            }
            .project-category h3 {
                color: #4CAF50;
                margin-bottom: 15px;
            }
            .project-card {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                border-left: 4px solid #4CAF50;
            }
            .project-card h4 {
                color: #333;
                margin: 0 0 15px 0;
            }
            .project-card ul {
                padding-left: 20px;
                margin-bottom: 15px;
                color: #666;
            }
            .project-card li {
                margin-bottom: 5px;
            }
            .project-link {
                display: inline-block;
                color: #4CAF50;
                text-decoration: none;
                font-weight: bold;
                margin-top: 10px;
                transition: color 0.3s ease;
            }
            .project-link:hover {
                color: #45a049;
                text-decoration: underline;
            }
        </style>
    """
    
    nav_html = f"""
        {nav_style}
        <header class="header">
            <nav class="nav-container">
                <a href="/" class="logo">Python Hub</a>
                <div class="nav-links">
                    <a href="/" class="nav-button">Home</a>
                    <a href="/about/" class="nav-button">About Us</a>
                    <a href="/contact/" class="nav-button">Contact Us</a>
                </div>
            </nav>
        </header>
    """
    return nav_html

def python(request):
    html = get_nav_html()
    html += '<div class="content">'
    for post in python_posts:
        html += f"<h1>{post['id']} - {post['title']}</h1>"
        html += f"<p>{post['content']}</p>"
        html += "<br>"
    html += '</div>'
    return HttpResponse(html)

def django(request):
    html = get_nav_html()
    html += '<div class="content">'
    for post in django_posts:
        html += f"<h1>{post['id']} - {post['title']}</h1>"
        html += f"<p>{post['content']}</p>"
        html += "<br>"
    html += '</div>'
    return HttpResponse(html)

def home(request):
    html = get_nav_html()
    html += """
        <div class="content">
            <h1>Python Learning Hub</h1>
            <div class="app-grid">
                <a href="/python/" class="app-button">
                    <div class="app-icon">🐍</div>
                    <div class="app-label">Python Basics</div>
                </a>
                <a href="/django/" class="app-button">
                    <div class="app-icon">🎯</div>
                    <div class="app-label">Django</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">📦</div>
                    <div class="app-label">Data Structures</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">⚛️</div>
                    <div class="app-label">Python + React</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">▲</div>
                    <div class="app-label">Python + Next.js</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">🌟</div>
                    <div class="app-label">Python + Vue</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">🔥</div>
                    <div class="app-label">FastAPI</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">🌐</div>
                    <div class="app-label">Flask</div>
                </a>
                <a href="#" class="app-button">
                    <div class="app-icon">🤖</div>
                    <div class="app-label">Machine Learning</div>
                </a>
            </div>
        </div>
    """
    return HttpResponse(html)

def about(request):
    html = get_nav_html()
    html += """
        <div class="about-container">
            <div class="profile-section">
                <h1>About Me</h1>
                <p>👋 Hi, I'm Fabian</p>
                <p>A passionate Software Developer from Nairobi, Kenya</p>
            </div>
            
            <h2>My Journey</h2>
            <p>As a software developer specializing in web applications, I've built my expertise around creating elegant solutions to complex problems. Currently, I'm expanding my tech stack by diving into Python and its ecosystem, particularly Django for web development.</p>
            
            <h2>Tech Stack</h2>
            <div class="tech-stack">
                <span class="tech-badge">HTML</span>
                <span class="tech-badge">CSS</span>
                <span class="tech-badge">JavaScript</span>
                <span class="tech-badge">Next.js</span>
                <span class="tech-badge">Nest.js</span>
                <span class="tech-badge">React</span>
                <span class="tech-badge">MySQL</span>
                <span class="tech-badge">Flutter</span>
                <span class="tech-badge">React Native</span>
                <span class="tech-badge">TypeORM</span>
                <span class="tech-badge">Prisma</span>
                <span class="tech-badge">Sequelize</span>
                <span class="tech-badge learning-badge">Python (Learning)</span>
                <span class="tech-badge learning-badge">Django (Learning)</span>
            </div>
            
            <h2>Projects</h2>
            <div class="projects-section">
                <div class="project-category">
                    <h3>Python Projects</h3>
                    <div class="project-card">
                        <h4>nohtyp.com</h4>
                        <p>A comprehensive Python learning platform built with Django. Features include:</p>
                        <ul>
                            <li>Interactive Python tutorials</li>
                            <li>Django framework guides</li>
                            <li>Integration examples with various frontend frameworks</li>
                        </ul>
                        <a href="/" class="project-link">View Project →</a>
                    </div>
                </div>
                
                <div class="project-category">
                    <h3>Other Projects</h3>
                    <div class="project-card">
                        <p>For my complete portfolio including web applications, mobile apps, and other projects, please visit:</p>
                        <a href="https://aminofabian.com" class="project-link" target="_blank">aminofabian.com →</a>
                    </div>
                </div>
            </div>
            
            <h2>What I Do</h2>
            <p>I specialize in building robust web applications, focusing on both functionality and user experience. My experience with various frameworks and tools allows me to choose the right technology for each specific project.</p>
            
            <h2>Project Management</h2>
            <p>Beyond coding, I'm well-versed in Agile and Scrum methodologies, enabling effective collaboration with cross-functional teams and timely delivery of high-quality solutions.</p>
            
            <h2>Community Involvement</h2>
            <p>I'm an active participant in tech conferences and hackathons, and I believe in contributing to open-source projects. These activities help me stay current with industry trends while giving back to the developer community.</p>
            
            <h2>Current Focus</h2>
            <p>I'm currently expanding my expertise by learning Python and Django, aiming to add these powerful tools to my tech stack. This journey allows me to bring even more value to my projects by combining Python's simplicity and Django's robustness with my existing skills.</p>
        </div>
    """
    return HttpResponse(html)

def contact(request):
    html = get_nav_html()
    html += """
        <div class="about-container">
            <h1>Contact Us</h1>
            <p>Get in touch with me:</p>
            <p>📧 Email: [Your Email]</p>
            <p>💼 LinkedIn: [Your LinkedIn]</p>
            <p>🐱 GitHub: [Your GitHub]</p>
            <p>📍 Location: Nairobi, Kenya</p>
        </div>
    """
    return HttpResponse(html)
