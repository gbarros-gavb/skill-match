tech_abbreviations = {
    'Amazon Web Services': 'AWS',
    'Google Cloud Platform': 'GCP',
    'Microsoft Azure': 'Azure',
    'IBM Cloud Services': 'IBM Cloud',
    'Oracle Cloud Infrastructure': 'Oracle Cloud',
    'Alibaba Cloud Services': 'Alibaba Cloud',
    'Representational State Transfer': 'REST',
    'Graphical User Interface': 'GUI',
    'Command Line Interface': 'CLI',
    'Application Programming Interface': 'API',
    'Software Development Kit': 'SDK',
    'Structured Query Language': 'SQL',
    'Not only SQL': 'NoSQL',
    'JavaScript Object Notation': 'JSON',
    'YAML Ain\'t Markup Language': 'YAML',
    'Test-Driven Development': 'TDD',
    'Behavior-Driven Development': 'BDD',
    'Continuous Integration/Continuous Deployment': 'CI/CD',
    'Extract, Transform, Load': 'ETL',
    'Artificial Intelligence': 'AI',
    'Machine Learning': 'ML',
    'Natural Language Processing': 'NLP',
    'Convolutional Neural Network': 'CNN',
    'Recurrent Neural Network': 'RNN',
    'Long Short-Term Memory': 'LSTM',
    'General Adversarial Networks': 'GAN'
}

tech_skills = [
    'AWS', 'Apache Airflow', 'React', 'Frontend', 'Backend', 'Python', 'Java', 'C++',
    'Ruby', 'Ruby on Rails', 'Flask', 'Django', 'JavaScript', 'TypeScript', 'Angular', 'Vue.',
    'HTML', 'CSS', 'Bootstrap', 'Tailwind CSS', 'SQL', 'NoSQL', 'MongoDB', 'PostgreSQL',
    'MySQL', 'SQLite', 'Docker', 'Kubernetes', 'Terraform', 'Ansible', 'Jenkins',
    'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Agile', 'Scrum', 'Kanban', 'TDD', 'BDD',
    'CI/CD', 'DevOps', 'Selenium', 'Junit', 'PyTest', 'Machine Learning', 'Deep Learning',
    'Data Science', 'TensorFlow', 'Keras', 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy',
    'Matplotlib', 'Seaborn', 'Tableau', 'Power BI', 'Big Data', 'Hadoop', 'Spark',
    'Flink', 'Kafka', 'RabbitMQ', 'Redis', 'Elasticsearch', 'GCP', 'Azure',
    'IBM Cloud', 'Oracle Cloud', 'Alibaba Cloud']

def replace_with_abreviations(text: str, abbreviations: dict) -> str:
    for phrase, abbreviation in abbreviations.items():
        text = text.replace(phrase, abbreviation)
    return text

def find__skills_in_text(text: str, skills: list) -> list:
    return [skill for skill in skills if skill in text]


test_text = "Preciso de ajuda com tecnologias Azure"

print(find__skills_in_text(replace_with_abreviations(text=test_text, abbreviations=tech_abbreviations), skills=tech_skills))