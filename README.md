## Print 📽

### Introduction and Objectives ⁉

The purpose of this project is to create a platform where the freshmen of Mauá´s Institute of Technology (IMT) can register for events and lectures, during the first week of enrollment. Using our platform they will be able to learn more about Mauá´s campus, infrastructure, and professors. They will also have the opportunity to participate in activities where they will meet fellow classmates.

This project is using Dev. Community Mauá's Clean Architecture template. It´s main objective is to provide a template for repositories that can be used as a starting point for new projects.

## Name Format 📛
### Files and Directories 📁

- Files have the same name as the classes
- snake_case 🐍 (ex: `./app/create_student_organization.py`)

### Classes 🕴
- #### Pattern 📟

    - CamelCase 🐫🐪

- #### Types 🧭

    - **Interface** starts with "I" --> `ICourseRepository` 😀
    - **Repository** have the same name as interface, without the "I" and the type in final (ex: `CourseRepositoryMock`)
    - **Controller** ends with "Controller" --> `CreateCourseController`🎮
    - **Usecase** ends with "Usecase" --> `CreateCourseUsecase` 🏠
    - **Viewmodel** ends with "Viewmodel" --> `CreateCourseViewmodel` 👀
    - **Presenter** ends with "Presenter" --> ``CreateCoursePresenter``🎁

### Methods 👨‍🏫

- snake_case 🐍
- Try associate with a verb (ex: `create_student_organization`, `get_student_organization`)

### Variables 🅰

- snake_case 🐍
- Avoid verbs

### Enums

- SNAKE_CASE 🐍
- File name ends with "ENUM" (ex: "STATE_ENUM")

### Tests 📄

- snake_case 🐍
- "test" follow by class name (ex: `test_create_student_organization`, `test_get_student_organization`)
    - The files must start with "test" to pytest recognition

### Commit 💢

- Start with verb
- Ends with emoji 😎

## Installation 👩‍💻

Clone the repository using template

### Create virtual ambient in python (only first time)

###### Windows

    python -m venv venv

###### Linux

    virtualenv -p python3.9 venv

### Activate the venv

###### Windows:

    venv\Scripts\activate

###### Linux:

    source venv/bin/activate

### Install the requirements

    pip install -r requirements-dev.txt

### Run the tests

    pytest

### To run local set .env file

    STAGE = TEST


## Contributors 💰🤝💰

- Carlos Henrique Lucena Barros - [barros-carlos](https://github.com/barros-carlos)
- Débora Witkowski - [DebWit](https://github.com/DebWit) 
- Leonardo Cazotto Stuber - [LCStuber](https://github.com/LCStuber)
- Mateus Capaldo Martins - [MatCMartins](https://github.com/MatCMartins)

## Special Thanks 🙏

- [Dev. Community Mauá](https://www.instagram.com/devcommunitymaua/)
- [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.amazon.com.br/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
- [Institute Mauá of Technology](https://www.maua.br/)



