
# Cover page/Identity Information

Assessment name: Final Assessment

Student name: Milan Ale

Student ID: 21096653

Practical class (date/time/venue): Monday / 12:00 - 2:00 / 314 220



# Introduction

Following the modularity principles, two programs—a Finding Season Program and a Temperature Check Program—were developed and are presented in this project report. These programs were created to show off how modular programming, which enables the creation of reusable and maintainable code, can be used effectively. Additionally, this report discusses the adoption of different testing approaches to ensure the reliability and robustness of the implemented programs.  
The integration of Git, a version control system, as a key tool for collaborative software development is also highlighted in this project report. Git's use made it possible for seamless integration of new features and bug fixes as well as efficient team collaboration and version tracking. Professionalism and ethics were also important factors to take into account when developing the project.  
This report gives a summary of the project's goals, methods, specifics of its execution, and outcomes. The difficulties encountered during the development process are also covered, along with the solutions used. An assessment of the project's performance that highlights the successes and potential areas for future improvement comes at the end of the report.  
Overall, this project report demonstrates the effective use of Git, various testing techniques, and the modularity principles in the development of two programs. It drives home the significance of professionalism and ethical considerations in software development, advancing industry best practices.


# Module Description

> Submodule: find_season()
> 
> Input: country, month (String)
> 
> Output: season(String)
>
> If country and month exist in the available data, then return season else return "Not found".

The purpose of this module is to find the season using the month and country inputs. To keep track of the seasons for various nations and months, it uses a nested dictionary called seasons. The module returns the appropriate season after receiving the country and month as inputs. To handle case insensitivity, it converts the input to lowercase. It retrieves the season related to the country and month if they are found in the seasons dictionary. It returns a "Not found" message if it cannot be found.

Assumptions: The module assumes that the input country and month will be provided as strings and follows a specific format. It assumes that the season for a given country and month is pre-defined and available in the seasons dictionary. If the input does not match any valid country or month in the dictionary, it assumes that the season is not found and returns a "Not found" message.


> Submodule: check_temperature()
>
> Input: city(String), time(String), temperature(Float)
>
> Output: message(String)
>
> If the temperature is greater than the average temperature and the difference is more than 5, then return an additional message otherwise return 'Above'. ElseIf the difference is less then, return 'Below', else return 'Not found'.

Based on the city, time, and temperature inputs, this module was developed to check the current temperature status. To keep track of the average temperatures for various cities and times, it uses the dictionary average_temperatures. The module compares the provided temperature with the typical temperature for the specified city and time after receiving the city, time, and temperature as inputs. If the temperature is higher, lower, or the difference is more than 5°C compared to the average temperature, it returns a message stating that information.

Assumptions: The module assumes that the input city and time will be provided as strings and follows a specific format. It assumes that the average temperatures for different cities and times are pre-defined and available in the average_temperatures dictionary. If the input does not match any valid city, time, or temperature in the dictionary, it assumes that the data is not found and returns a "Not found" message.

The module descriptions were unchanged following the refactoring. The process of refactoring concentrated on enhancing the modularity, readability, and structure of the code. The intended tasks, behaviors, inputs, or outputs of the modules were not altered in any way.

# Modularity

```
# Convert the country and month to lowercase to handle case-insensitivity
    country = country.lower()
    month = month.lower()
    
    # Check if the country and month are in the seasons dictionary
    if country in seasons and month in seasons[country]:
        season = seasons[country][month]
        return season
    else:
        invalid = f"Not found"
        return invalid
```

```
# Convert the city and time to lowercase to handle case-insensitivity
    city = city.lower()
    time = time.lower()

    # Check if the city and time are in the average_temperatures dictionary
    if city in average_temperatures and time in average_temperatures[city] and temperature:
        average_temp = average_temperatures[city][time]
        difference = round(float(temperature) - average_temp, 2)
        if float(temperature) > average_temp:
            if difference > 5:
                message = f"The temperature in {city} {time} is {temperature}°C, which is {difference}°C above the average temperature."
                return message
            else:
                result1 = f"Above"
                return result1
        else:
            result2 = f"Below"
            return result2
    else:
        result = f"Not found"
        return result
```

The find_season() and check_temperature() modules demonstrate several modularity concepts in their implementation. These modules are a part of a larger program, the main program, which receives input from the console and passes it as parameters to the corresponding function calls. The desired output is then generated by printing the returned values. 

In these modules a specific functionalities are encapsulated within each module. While check_temperature() assesses the temperature status based on the city, time, and temperature inputs, find_season() determines the season based on the country and month. This encapsulation allows for modular development and maintenance of the code, making it easier to understand and modify.

By giving the modules straightforward interfaces, abstraction is made possible. The required inputs and the expected output type are both specified in the function signatures. By hiding the internal implementation details of the modules, this abstraction enables the user to interact with them without having to understand the underlying logic.


The following features are included in the code review checklist:

1. Check if the code is divided into meaningful modules and if each module has a clear purpose.
2. Make sure the input parameters are properly validated and handled to prevent unexpected errors.
3. Review the usage of data structures such as dictionaries to store and retrieve relevant information.
4. Check the code for adherence to coding standards, proper indentation, and understandable variable and function names.
5. Check if appropriate error handling mechanisms are in place to handle invalid input or unexpected situations.


The review using the checklist revealed the following results:

1. Both modules demonstrate clear and focused functionality, addressing specific tasks related to season finding and temperature checking.
2. To handle case insensitivity, the code handles input validation by changing inputs to lowercase, ensuring consistency.
3. Dictionary-based data structures make it possible to store and retrieve relevant data for module operations quickly and effectively.
4. The use of meaningful variable and function names, consistent indentation, and proper coding practices all contribute to the code's readability and maintainability.
5. When input does not match any valid data in the dictionaries, the modules handle the situation by displaying a clear "Not found" message.

By conducting the review and making sure the checklist is followed, the code demonstrates good modularity, proper input handling, efficient data structure usage, code style, readability, and error handling, leading to a reliable and maintainable software solution.

To run the production code containing the 'find_season()' and 'check_temperature()' modules, a main file 'main.py' is created which takes the keyboard input from users and passes the input as parameters by calling the functions present in these modules. Then, the following steps needs to be followed: 

1. Open a command prompt or terminal.
2. Navigate to the directory where the 'main.py' file is located.
3. Run the code using the command: 'python main.py'.



# Black-box Test Cases

### **Equivalence Partitioning for find_season module**

| Category | Test Data| Expected Result|
| -------- | -------- | ---------------|
| Valid Equivalence Class: Country and Month exist in available data | country='Australia', month='December'| ['Summer','Birak'] |
| Invalid Equivalence Class: Country or Month does not exist in the available data | country='Denmark', month='March' | 'Not found' |
| Invalid Equivalence Class: Empty Country or Month | country=' ', month='June' | 'Not found' |
| Invalid Equivalence Class: Country or Month Invalid Input Type (eg: numeric input) | country=123, month='july' | 'Not found' |

These test cases include a variety of inputs, such as various countries and months. They are designed to verify that, given the inputs for the given country and month, the find_season() module returns the appropriate season. Each test case represents a unique set of inputs and the expected output for those inputs. The test cases include situations where the output is a single season or a list of seasons, as well as situations where the country or month is not found in the seasons dictionary and the output is "Not found.". By creating these test cases, we make sure the module correctly handles a variety of input configurations and produces the desired outcomes.


### **Equivalence Partitioning for check_temperature module**

| Category | Test Data| Expected Result|
| -------- | -------- | ---------------|
| Test case for difference more than 5 | city='Perth', time='morning', temperature=25| 'additional message' |
| Test case for 'Above' | city='Adelaide', time='evening' temperature=25 | 'Above' |
| Test case for 'Below' | city='Perth', time='evening' temperature=15 | 'Below' |
| Test case for Invalid data | city='Norway', time='ale' temperature=6653 | 'Not found' |

By offering various input combinations, these test cases demonstrate the check_temperature() module's functionality. Each test case represents a specific situation in which the module, given the inputs for the city, time, and temperature, should return the correct temperature status. The test cases include scenarios where the temperature is above, below, or when the city or time cannot be found in the dictionary of average_temperatures, resulting in the output "Not found.". One of the test cases gives an additional message as an output if the difference between the given temperature and the average temperature is more than positive 5. We make sure the module accurately handles various input combinations and provides the anticipated temperature status by creating these test cases.

These "black-box" test cases cover a range of scenarios and input combinations in order to verify the correctness and robustness of the modules. They offer a methodical approach to testing the modules' functionality without taking into account the specifics of their internal implementation.


# White-box Test Cases

**In "White Box" testing, test cases are based on the paths through a method/function.**

White-box testing ensures that we test each path - each possible way through the production code. Each path becomes a test case.

White-box testing seeks to assess the accuracy and efficacy of the code itself, as opposed to black-box testing, which is concerned with testing the functionality of the software without knowledge of its internal workings. It involves testing specific code branches, paths, and functions to make sure they work as intended and can handle a range of inputs and scenarios.

### **Test cases for find_season module**

| Path | Test Data| Expected Result|
| ---- | -------- | ---------------|
| Enter the 'if' condition | country='Australia', month='June'| ['Winter','Makuru'] |
| Do not enter the 'if' condition | country='France', month='September' | 'Not found' |

### **Test cases for check_temperature module**

| Path | Test Data| Expected Result|
| ---- | -------- | ---------------|
| Enter the third 'if' condition | city='Perth', time='morning', temperature=25 | 'additional message' |
| Enter the first 'else' condition | city='Perth', time='morning', temperature=20 | 'Above' |
| Enter the second 'else' condition | city='Adelaide', time='evening', temperature=19 | 'Below' |
| Enter the outer 'else' condition | city='Norway', time='ale', temperature=6653 | 'Not found' |


White-box testing focuses on the internal implementation and structure of the software. It supports a thorough testing approach by helping to find flaws, verify the correctness of the code, and provide insights into its behaviour and performance.


# Test Implemtation and Execution

The test cases are categorized by test type (BB for black-box testing and WB white-box testing). Following these techniques, four test codes are developed where two of them falls under black-box testing for each module while the other two are white-box testing. To run these test code for the find_season() and check_temperature() modules, follow these steps:

1. Open the file containing the test code in your preferred editor or IDE.
2. Make sure the production code file (containing the find_season() and check_temperature() functions) is in the same directory as the test code file.
3. Run the test code by executing the file or using the appropriate command. For example, in Python, you can use the command 'python test_code.py' to run the test code.


Reviewing the test results reveals that every function's test case passed, demonstrating its proper functionality. It is crucial to remember that one test case did not produce the desired outcome, leading to a failed result. The failed test case was carefully examined, and adjustments were made to guarantee the intended result was realized. To increase the dependability and accuracy of the code, it is imperative to continuously work toward improvement and address any inconsistencies.

![assertion_error](/Screenshots/assertion_error.png "Screenshot1")

![check_temperature_difference](/Screenshots/check_temperature_difference.png "Screenshot2")

![main_check_temperature](/Screenshots/main_check_temperature.png "Screenshot3")

The first screenshot above displays an assertion error encountered during the execution of the test code for the 'check_temperature' module. This error occurred because the 'check_temperature()' function did not return the expected message, as shown in the second screenshot. The discrepancy arises from the fact that the test code expected the difference between the user-input temperature and the average temperature to be a number rounded to two decimal places. However, the actual code returned a difference of 6.800000000000001, as depicted in the third screenshot. To address this issue, a modification was made to the code by utilizing the built-in 'round()' function to round the difference to two decimal places. This adjustment ensures that the test case produces the desired outcome.

![solved_check_temperature](/Screenshots/solved_check_temperature.png "Screenshot4")


## **(EP: Equivalence Partitioning, BVA: Boundary Value Analysis, BB: Black-box, WB: White-box)**

| Module Name | BB Test Design(EP) | BB Test Design (BVA) | WB Test Design | EP Test Code (Implemented/Run) | BVA Test Code (Implemented/Run) | White-Box Testing (Implemented/Run) |
| ---- | ---- | ---- | ---- | ---- | ---- | ----|
| 'find_season' | Done | Not Done | Done | Done | Not Done | Done |
| 'check_temperature' | Done | Not Done | Done | Done | Not Done | Done |



# Version Control

Version control  provides features such as commit logs, which record the details of each change made to the code, including who made the change and why. This allows for traceability and accountability in the development process. Version control is essential in a professional software project for upholding code quality, facilitating collaboration, and ensuring a seamless development workflow. It encourages openness, responsibility, and the capacity to effectively monitor and manage change.

Overall, version control is a crucial tool for software development because it offers a structured method for handling code changes and makes it possible for team members to collaborate effectively.


# Ethics

a. The code can have negative effects if it is not used with integrity and professionalism. In the scenario of the find_season() and check_temperature() modules being used in a large software project, the following ethical issues could arise:

1. Privacy Violation: It is crucial to handle user data with the utmost care and respect for privacy if the software project entails collecting user data, such as their location or personal information. Inaction could result in privacy violations and the potential misuse of sensitive information.
2. Results that are incorrect: The find_season() and check_temperature() modules rely on predefined data sets and presumptions regarding temperature ranges and seasons. Results may be inaccurate if the assumptions are not verified or the data is not updated on a regular basis. This can be a problem if the software project heavily relies on these modules to make crucial decisions regarding scheduling or resource allocation.
3. Bias and Discrimination: If the data sets utilized to determine the seasons or temperature ranges are not diverse and representative, the code may unintentionally introduce bias or discrimination. Due to their location or timing, certain groups of people may be treated unfairly or excluded as a result.
4. Lack of Accessibility: If the code fails to take into account accessibility requirements, such as offering alternate formats for output or accommodating users with disabilities, it may put up barriers and prevent some people from accessing the information provided by the modules.
5. Vulnerabilities in the code's design and implementation caused by inadequate attention to security procedures can leave the code open to attack from malicious actors. Unauthorized access, data breaches, or service interruption may result from this.
6. Intellectual Property Violation: If the code or data sets used in the modules violate intellectual property rights, such as copyright or licensing restrictions, it may result in legal problems and harm the software project's reputation.
7. Absence of Transparency: Misunderstandings and potential abuse can result from a lack of clear documentation and disclosure about the code's constraints and underlying presumptions. Users should have a thorough understanding of how the code operates and the variables that could affect its results.

b. To avoid ethical and professional issues in the software proposed in this assignment, the following suggestions can be implemented based on the ACS or IEEE-CS Ethical guidelines:

1. Conduct Periodic Ethical Reviews: Conduct ongoing ethical reviews of the software project to find any potential ethical issues or inconsistencies. To do this, one must evaluate the data sources, ensure the security and privacy of the data, and address any bias or discrimination present in the code or its results. The project can reduce potential harm and guarantee ethical compliance by proactively addressing ethical issues.
2. Encourage open discussions about ethical issues and offer training and direction on ethical principles and guidelines to foster a culture of ethical decision-making throughout the project. As they design, implement, and use the code, project participants will be better able to make ethical decisions.

The software project can uphold moral standards, safeguard user privacy, guarantee accuracy and fairness in the code's outputs, prioritize security, respect intellectual property rights, encourage accessibility, and give users transparent information by incorporating these recommendations into the development process.


# Discussion

I created and implemented modules as part of this assignment to meet the necessary functionalities. My main focus has been on implementing modularity principles, such as grouping related tasks into modules, defining distinct input and output mechanisms, and ensuring code reuse. To ensure thorough coverage of various scenarios and to verify the accuracy and robustness of the code, I have created both black-box and white-box test cases. To create efficient test cases, I took into account equivalence partitioning methodology. I have found and fixed potential problems through testing, enhancing the code's dependability and accuracy.

I could have done more testing, in terms of file inputs and file outputs, to find any buried bugs or performance problems, which would have further enhanced my work. I could have added error handling and exception mechanisms as well to deliver more detailed and user-friendly error messages. The overall stability and usability of the code would benefit from these improvements.

Overall, this assignment has given me useful experience in designing modular code, putting testing strategies into practice, and taking ethical considerations into account. It has reaffirmed the value of following best practices in software engineering, such as modularity, testing, and ethical considerations. I'll keep using these guidelines in my work going forward to make sure that superior, trustworthy, and moral software solutions are created.



# References 

1. School of Electrical Engineering, Computing and Mathematical Sciences (EECMS). (2023). Lecture 7: Modularity[PDF]. Blackboard. https://lms.curtin.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_128974_1&content_id=_10898186_1
2. School of Electrical Engineering, Computing and Mathematical Sciences (EECMS). (2023). Lecture 6: Testing (part 1)[PDF]. Blackboard. https://lms.curtin.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_128974_1&content_id=_10898182_1
3. School of Electrical Engineering, Computing and Mathematical Sciences (EECMS). (2023). Lecture 9: Test Fixtures and White-box Testing[PDF]. Blackboard. https://lms.curtin.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_128974_1&content_id=_10898191_1
4. School of Electrical Engineering, Computing and Mathematical Sciences (EECMS). (2023). Lecture 9: Ethics and Professionalism[PDF]. Blackboard. https://lms.curtin.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_128974_1&content_id=_10898195_1
5. School of Electrical Engineering, Computing and Mathematical Sciences (EECMS). (2023). Lecture 5: Version Control[PDF]. Blackboard. https://lms.curtin.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_128974_1&content_id=_10898178_1
6. Loeliger, J. (2009). Version Control with Git Powerful tools and techniques for collaborative software development. Sebastopol, O'Reilly Media.

