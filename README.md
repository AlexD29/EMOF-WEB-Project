Imagini puteti lua de pe link-ul asta: https://tophinhanhdep.com/anh-dep/color-hd-wallpapers/

https://github.com/rick4470/IEEE-SRS-Tempate#readme
1.1x?    1.2x?    1.3x    1.4v    2.1?    2.2v    2.3v
2.4v    2.5?    2.6?    2.7? Dependencies v
3.1v Poze/img    3.2x    3.3x?    3.4x?
4..v tehnic specific cam cum vrem sa facem (link catre poze 3.1)
5.1x? daca vrem ceva optimizari, sa ne jucam cu deployment
5.2x    5.3v "dorim sa tratam cele mai intalnite atacuri ..."
5.4?    5.5?

# Software Requirements Specification
## For  EMOF
Prepared by <author>
<date created>

Table of Contents
=================
  * [Revision History](#revision-history)
  * [Introduction](#1-introduction)
    * 1.4 [Product Scope](#14-product-scope)
    * 1.5 [References](#15-references)
  * [Overall Description](#overall-description)
    * 2.1 [Product Perspective](#21-product-perspective)
    * 2.2 [Product Functions](#22-product-functions)
    * 2.3 [User Classes and Characteristics](#23-user-classes-and-characteristics)
    * 2.4 [Operating Environment](#24-operating-environment)
    * 2.5 [Design and Implementation Constraints](#25-design-and-implementation-constraints)
    * 2.6 [User Documentation](#26-user-documentation)
    * 2.7 [Assumptions and Dependencies](#27-assumptions-and-dependencies)
  * [External Interface Requirements](#external-interface-requirements)
    * 3.1 [User Interfaces](#31-user-interfaces)
    * 3.2 [Hardware Interfaces](#32-hardware-interfaces)
    * 3.3 [Software Interfaces](#33-software-interfaces)
    * 3.4 [Communications Interfaces](#34-communications-interfaces)
  * [System Features](#system-features)
    * 4.1 [System Feature 1](#41-system-feature-1)
    * 4.2 [System Feature 2 (and so on)](#42-system-feature-2-and-so-on)
  * [Other Nonfunctional Requirements](#other-nonfunctional-requirements)
    * 5.1 [Performance Requirements](#51-performance-requirements)
    * 5.2 [Safety Requirements](#52-safety-requirements)
    * 5.3 [Security Requirements](#53-security-requirements)
    * 5.4 [Software Quality Attributes](#54-software-quality-attributes)
    * 5.5 [Business Rules](#55-business-rules)
  * [Other Requirements](#other-requirements)
* [Appendix A: Glossary](#appendix-a-glossary)
* [Appendix B: Analysis Models](#appendix-b-analysis-models)
* [Appendix C: To Be Determined List](#appendix-c-to-be-determined-list)


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

### 4.2 System Feature 2 (and so on)

## Other Nonfunctional Requirements
### 5.3 Security Requirements
We want to prevent the most common attacks such as cross-site scripting, SQL injection, distributed denial of service.
