Imagini puteti lua de pe link-ul asta: https://tophinhanhdep.com/anh-dep/color-hd-wallpapers/

# Software Requirements Specification
## For  EMOF
Prepared by Brassat Alexandru, Duca Alexandru, Popa Stefan

Table of Contents
=================
  * [Revision History](#revision-history)
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
    * 4.1 [System Feature 1](#41-system-feature-1)
    * 4.2 [System Feature 2 (and so on)](#42-system-feature-2-and-so-on)
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
poze cu paginile principale
![alt text](http://url/to/img.png)
### 3.3 Software Interfaces
SQL Lite for Database to keep user accounts and their forms.
## System Features
### 4.1 System Feature 1
Don’t really say “System Feature 1.” State the feature name in just a few words.
4.1.1   Description and Priority
 Provide a short description of the feature and indicate whether it is of High, Medium, or Low priority. You could also include specific priority component ratings, such as benefit, penalty, cost, and risk (each rated on a relative scale from a low of 1 to a high of 9).
4.1.2   Stimulus/Response Sequences
 List the sequences of user actions and system responses that stimulate the behavior defined for this feature. These will correspond to the dialog elements associated with use cases.
4.1.3   Functional Requirements
 Itemize the detailed functional requirements associated with this feature. These are the software capabilities that must be present in order for the user to carry out the services provided by the feature, or to execute the use case. Include how the product should respond to anticipated error conditions or invalid inputs. Requirements should be concise, complete, unambiguous, verifiable, and necessary. Use “TBD” as a placeholder to indicate when necessary information is not yet available.
 
Each requirement should be uniquely identified with a sequence number or a meaningful tag of some kind.

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

### 4.4 Viewing form's statistics

#### 4.4.1 Description
The LOGGED IN user can view the statistics of an own form.
#### 4.4.2 Stimulus/Response Sequences
The quiz owner will be able to see the statistics in the form of a list of "interesting things" .The algorithm based on Artificial Intelligence will decide what is most interesting to watch and based on those recommendations, different appropriate representations of the data will be displayed. Besides the "list of interesting things", there will also be a simpler list composed of the statistics of each question.
#### 4.4.3 Functional Requirements
[NOT YET IMPLEMENTED]

### 4.5 Viewing  Created Forms

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

## Other Nonfunctional Requirements
### 5.3 Security Requirements
We want to prevent the most common attacks such as cross-site scripting, SQL injection, distributed denial of service.
