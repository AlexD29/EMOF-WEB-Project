# Software Requirements Specification
## For  EMOF
Prepared by Brassat Alexandru, Duca Alexandru, Popa Stefan

Table of Contents
=================
  * [Introduction](#1-introduction)
    * 1.4 [Product Scope](#14-product-scope)
  * [Overall Description](#overall-description)
    * 2.2 [Product Functions](#22-product-functions)
    * 2.3 [User Classes and Characteristics](#23-user-classes-and-characteristics)
    * 2.4 [Operating Environment](#24-operating-environment)
  * [External Interface Requirements](#external-interface-requirements)
    * 3.1 [User Interfaces](#31-user-interfaces)
    * 3.3 [Software Interfaces](#33-software-interfaces)
  * [System Features](#system-features)
    * 4.1 [Filling out the form](#41-filling-out-the-form)
    * 4.2 [Creating a form](#42-creating-a-form)
    * 4.3 [Editing a form](#43-editing-a-form)
    * 4.4 [Viewing form statistics](#44-viewing-form-statistics)
    * 4.5 [Viewing  Created Forms](#45-viewing-created-forms)
    * 4.6 [Explore Forms](#46-explore-forms)
  * [Other Nonfunctional Requirements](#other-nonfunctional-requirements)
    * 5.3 [Security Requirements](#53-security-requirements)


## 1. Introduction
### 1.4 Product Scope
A Web application that allows users to provide feedback for a certain "thing" (event, person, geographic place, product, service, artistic artifact, etc.) in an anonymous manner.
## Overall Description
### 2.2 Product Functions
Some major functionalities of the application are the creation of accounts for users, the creation and completion of forms and the visualization in an attractive way of the statistics generated based on the completion of forms.
### 2.3 User Classes and Characteristics
Anonymous users who can only fill out forms and users who have a created account and can create forms.
### 2.4 Operating Environment
Frontend was build using HTML, CSS and JAVASCRIPT and the backend server will be implemented in Python.
## External Interface Requirements
### 3.1 User Interfaces
Landing Page:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232017.png?raw=true)
Sign up:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232033.png?raw=true)
Log in:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232025.png?raw=true)
View Forms:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/README-pictures/all_forms.png?raw=true)
Explore Forms:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/README-pictures/explore_formulars.png?raw=true)
Create Form:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232206.png?raw=true)
Complete Form:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232116.png?raw=true)
View Statistics:
![alt text](https://github.com/AlexD29/EMOF-WEB-Project/blob/main/Images/Screenshot%202023-04-09%20232155.png?raw=true)

### 3.3 Software Interfaces
SQL Lite for Database to keep user accounts and their forms.
## System Features
### 4.1 Filling out the form
#### 4.1.1 Description
The user fills in the form using the Plutchick wheel and/or expressing himself in his own words.
#### 4.1.2 Stimulus/Response Sequences
The user can use the dedicated Start, Next, Finish and Back buttons to navigate through the form.You can see the progress of the form by looking at the top of the page, more precisely at the progress bar. He answers the questions by clicking on the corresponding emotions on the wheel or by entering actual phrases in the "Write what you think" section.
If you have changed your mind about the emotion chosen for a certain question, you can deselect it by clicking again on the emotion that wants to be deleted from the list.
You can see the emotions already selected in the "What you feel" section. At the end of the form, a "Back to Explore" button will appear, which when pressed will redirect the user to the list of public forms .
#### 4.1.3 Functional Requirements
[NOT YET IMPLEMENTED] The user will not be able to submit the form if he has not answered at least one question.An answer to the question is valid if at least one emotion is chosen on the wheel or the recognition system will detect at least one emotion based on what the user entered as an expression in words.

### 4.2 Creating a form
#### 4.2.1 Description
The LOGGED IN user can create a form .
#### 4.2.2 Stimulus/Response Sequences
Fields such as name, tags and questions can be filled in .To create a field for a question, press the "Add Question" button.To delete a field for a question, press the "Delete Question" button .After completing the form, press the "Done" button .When pressed, a check will be made for each field and if all meet the requirements then the form will be created, otherwise a notification will appear telling you which field was wrong.
#### 4.2.3 Functional Requirements
The form is valid and can be sent if it meets the following conditions : the name of the form must necessarily contain between 6 and 100 characters , there should be at least one question in the form and a maximum of 15 questions and each question must contain at least 20 and at most 1000 characters . If the "Done" button has been pressed and the form has been validated correctly, a notification will appear saying that the form has been created and will redirect you to the forms page that the user can manage.

### 4.3 Editing a form
#### 4.3.1 Description
The LOGGED IN user can edit a form that he created.
#### 4.2.2 Stimulus/Response Sequences
The interaction is the same as the "Creating a form" page , but the difference is that the already existing data of the form will be automatically loaded into the fields, and the user can change them at will, respecting the requirements of each field.
#### 4.3.3 Functional Requirements
Same as [4.2.3](#423-functional-requirements)

### 4.4 Viewing form statistics
#### 4.4.1 Description
The LOGGED IN user can view the statistics of an own form.
#### 4.4.2 Stimulus/Response Sequences
The quiz owner will be able to see the statistics in the form of a list of "interesting things" .The algorithm based on Artificial Intelligence will decide what is most interesting to watch and based on those recommendations, different appropriate representations of the data will be displayed. Besides the "list of interesting things", there will also be a simpler list composed of the statistics of each question.
#### 4.4.3 Functional Requirements
[NOT YET IMPLEMENTED]

### 4.5 Viewing Created Forms
#### 4.5.1 Description
The User will be able to view their unpublished, published or closed forms.
#### 4.5.2 Stimulus/Response Sequences
The User will interact with the "admin" page, which will list all of their forms. Those can be grouped in the three categories mentioned above, and can be sorted by category by using a series of buttons on the left side of the page. For all forms, the user will be able to perform certain actions (such as edit, publish, close, view statistics, delete), according to the state the forms are in (draft, active, closed). 
#### 4.5.3 Functional Requirements
The user must be logged in to view their forms.

### 4.6 Explore Forms
#### 4.6.1 Description
All users (anonymous or not) will be able to participate in public forms made by other users. The forms will be grouped by multiple criteria. 
#### 4.6.2 Stimulus/Response Sequences
The User will browse the page and, when a certain form catches their attention, will be able to join the form. 
#### 4.6.3 Functional Requirements
In order for this page to be functional, it requires a number of public forms. In the case when there are none, an informative message will be shown.

### 4.7 Sign Up
#### 4.7.1 Description
Any user has the option to create an account, but it's not mandatory as the user can use the app and explore forms without an account. Creating an account allows the user to acces other features like Creating forms or Viewing Statistics about his completed forms.
#### 4.7.2 Stimulus/Response Sequences
If he wants to have permission to the features mentioned before, the user can easily and fast create an account by pressing the button 'Sign up' on the Landing page. He will be asked to enter an email address, an username and a password and then he will be redirected directly to his admin page, giving him acces to the features.
#### 4.7.3 Functional Requirements
To be able to access the 'Sign up' option, the user must not already be connected to an account in the application first and then must enter a valid email address and a username and a password of at least 8 characters.

### 4.8 Log in - Log out
#### 4.8.1 Description
If the user has created an account in the application, he will always be able to access it through the 'Log in' feature. It will also be possible to disconnect from the account using the 'Log out' option.
#### 4.8.2 Stimulus/Response Sequences
Every time the user wants to access his created account, he will be able to do it easily by entering either the username or the email. Also, if he somehow forgots his password, he will be able to enter his email address where he will be sent a verification link that he will have to access in order to recover his account. If the user wishes this, the data entered by him can be retained to keep him connected all the time to his account or he can 'Log out' every time he leaves the application.
#### 4.8.3 Functional Requirements
To be able to acces the 'Log in' and 'Log out' features, the user should firstly create an account using the 'Sign up' feature.

## Other Nonfunctional Requirements
### 5.3 Security Requirements
We want to prevent the most common attacks such as cross-site scripting, SQL injection, distributed denial of service.
