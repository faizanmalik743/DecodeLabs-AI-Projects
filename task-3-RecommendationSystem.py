from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Job roles dataset
jobs = {
    "title": [
        "Data Scientist",
        "Machine Learning Engineer",
        "Backend Developer",
        "Frontend Developer",
        "DevOps Engineer",
        "Cloud Architect",
        "Cybersecurity Analyst",
        "AI Research Scientist",
        "Full Stack Developer",
        "Data Analyst"
    ],
    "skills": [
        "python sql machine learning data analysis statistics pandas numpy",
        "python tensorflow pytorch deep learning neural networks algorithms",
        "python java sql apis rest databases backend server",
        "javascript html css react frontend ui ux web",
        "aws docker kubernetes linux ci cd automation cloud",
        "aws cloud azure infrastructure networking automation devops",
        "networking security firewall linux ethical hacking encryption",
        "python research deep learning algorithms mathematics statistics",
        "javascript python html css sql react backend frontend",
        "sql excel python data visualization statistics reporting"
    ]
}

df = pd.DataFrame(jobs)

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()
job_matrix = vectorizer.fit_transform(df["skills"])

# Take user input
print("=== AI Tech Stack Recommender ===\n")
print("Enter your skills one by one (minimum 3):\n")

user_skills = []
for i in range(1, 4):
    skill = input(f"Skill {i}: ").strip().lower()
    user_skills.append(skill)

user_profile = " ".join(user_skills)

# Transform user input and calculate similarity
user_vector = vectorizer.transform([user_profile])
similarity_scores = cosine_similarity(user_vector, job_matrix)[0]

# Add scores to dataframe and sort
df["match_score"] = similarity_scores
top_recommendations = df.sort_values("match_score", ascending=False).head(3)

# Display results
print("\n=== Top 3 Recommended Career Paths ===\n")
for i, (_, row) in enumerate(top_recommendations.iterrows(), 1):
    print(f"{i}. {row['title']}")
    print(f"   Match Score: {row['match_score']:.2f}\n")
