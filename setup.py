import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__varsion__ = "0.0.0"

REPO_NAME = "text-summarizer"
AUTHOR_NAME = "yatin-kundra"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ykundra44@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __varsion__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    Long_description = long_description,
    Long_description_content ="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        f"Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
},
    package_dir={"": "src"},
    packages=setuptools. find_packages(where="src")
)