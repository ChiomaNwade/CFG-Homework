CHIOMA SUSAN NWADE 
FOUNDATION ASSESSMENT 2 

1.1.	SDLC

It stands for Software Development Life Cycle which is a well-defined process used in software engineering to guide the development, deployment, and maintenance of software applications. SDLC defines the complete cycle of development as shown below: 


1.2.	In Python, if an attempt is made to divide a number by zero, a ZeroDivisionError occurs. It is an arithmetic error that arises because division by zero is not permissible in mathematics, and Python raises a ZeroDivisionError exception to indicate this.

1.3.	The Git command responsible for transferring code from the local repository to the remote repository is known as "git push." 

By executing this command, you can upload or push your local commits and branch updates to the corresponding remote repository. It enables you to share your code changes with others and facilitates collaborative work. To use the command, you typically specify the name of the remote repository and the target branch. For instance, if you want to push code to the "main" branch of the "origin" remote repository, you would use the command "git push origin main." Prior to executing the push command, ensure that you have committed your changes using "git commit" and possess the necessary permissions and access rights for the remote repository.

1.4.	In a database, NULL represents the absence or lack of a value in a field or column. It signifies unknown or missing data and is different from an empty string or zero. Handling NULL values correctly is important for accurate data representation and avoiding errors in database operations.

1.5.	The Scrum Master in the Scrum framework has two main responsibilities:
a.	Ensuring Effective Scrum Process: The Scrum Master facilitates the Scrum process, overseeing ceremonies like daily stand-ups, sprint planning, reviews, and retrospectives. They guide the team in adhering to Scrum principles and practices, while also removing any obstacles that hinder progress.

b.	Guiding and Coaching the Team: The Scrum Master supports the development team by coaching them on Scrum practices and fostering self-organization. They encourage collaboration, resolve conflicts, and promote a transparent and trusting environment that enables the team to deliver high-quality work.

1.6.	Debugging methods:
a.	Error Handling and Exception Handling: Implementing proper error and exception handling mechanisms within the code to catch and handle errors gracefully. This involves using try-catch blocks to capture exceptions and handle them appropriately, providing meaningful error messages or fallback mechanisms. 

Times when they can be used: 
•	When you want to handle and recover from errors or exceptions gracefully.
•	To provide meaningful error messages or fallback mechanisms to users.
•	During runtime debugging to capture and handle specific exceptions.


b.	Breakpoints: Breakpoints are markers set by developers within the source code to pause the program's execution at a specific line or condition. When the program reaches a breakpoint, it halts, allowing the developer to inspect variables, step through code, and analyze the state of the program. Breakpoints are commonly used in integrated development environments (IDEs) and debugging tools. They are effective for pinpointing the cause of specific issues and understanding the program's behavior at a granular level.

Times when they can be used: 
•	You want to pause the program's execution at a specific line or condition to analyze its state.
•	When stepping through code to identify the cause of a specific issue or bug.
•	When using an integrated development environment (IDE) or debugging tools that support breakpoints.

1.7.	ValueError exception handling can be used In the case where either the price or cash_given argument is negative, it contradicts the assumption made by the function, which requires non-negative values. For instance, if the price is -10 or the cash_given is -20, an error will be triggered. To catch the exception, we can execute the following block of code:

def can_pay(price, cash_given):
    try:
        if price < 0 or cash_given < 0:
            raise ValueError("Price and cash given must be non-negative.")
        return cash_given >= price
    except ValueError as error:
        print(f"Error: {error}")
        return False

1.8.	Git branching is a functionality in Git that enables the creation of separate lines of development within a repository. It allows developers to work on different features, fixes, or experiments simultaneously without affecting the main codebase. Here's how Git branching is used:

1.	Creation: Developers create new branches from an existing branch (typically the main branch) to establish independent workspaces for making changes.

2.	Switching: Developers switch to the desired branch using the `git checkout` command to focus on working within that specific branch.


3.	Development: Changes are made within the branch, including modifications to files, additions of new features, bug fixes, or experimental code. Commits track and save these changes in the branch's history.

4.	Isolation: Branches ensure isolation, allowing developers to work independently on their respective features or fixes. This prevents conflicts that may arise when multiple developers modify the same code simultaneously.

5.	 Collaboration and Review: Branches can be pushed to a remote repository, enabling collaboration with other team members. Peers can review the branch, provide feedback, and suggest improvements.

6.	 Integration: When changes in a branch are ready to be incorporated into the main codebase, developers can merge the branch back into the main branch or rebase it onto the latest commits. This integrates the changes effectively.

7.	Iteration: Developers can create new branches and repeat the process to work on different features or enhancements. This iterative branching workflow facilitates agile development and efficient management of parallel work streams.


1.9.	Restaurant ordering system.

a. Key Requirements of a Restaurant Ordering System:
- Menu Presentation: Displaying a visually appealing and user-friendly menu with item descriptions, images, and allergen information.
- Order Management: Managing incoming orders, tracking their status, and providing real-time updates to customers and staff.
- Table Reservations: Allowing customers to make table reservations, specifying the date, time, and number of guests.
- Special Requests: Accommodating special requests or dietary restrictions from customers, such as vegetarian, gluten-free, or nut-free options.
- Loyalty Program: Implementing a loyalty program to reward repeat customers and provide incentives for future orders.
- Inventory Management: Monitoring ingredient availability and automatically updating menu items based on stock levels.
- Multiple Payment Methods: Supporting various payment options like credit/debit cards, mobile wallets, or cash on delivery.
- Multi-Language Support: Providing language options for customers to view the menu and place orders in their preferred language.
- Integration with Delivery Services: Integrating with third-party delivery platforms (e.g., Grubhub, Deliveroo) for seamless order delivery.

b. Main Considerations and Challenges:
- Scalability: Designing a system that can handle a large volume of orders, especially during peak hours.
- Seamless User Experience: Ensuring an intuitive and easy-to-navigate interface for customers to browse the menu, customize orders, and complete payments smoothly.
- Data Security: Implementing robust security measures to protect customer data, payment information, and sensitive business data.
- Synchronization: Ensuring synchronization between front-of-house, kitchen, and delivery staff to minimize order processing and delivery time.
- Integration with External Systems: Establishing seamless integration with external systems such as POS (Point of Sale), inventory management, and accounting systems.
- Performance Optimization: Optimizing system performance to handle simultaneous user requests and minimize response times.
- Adaptability: Designing a flexible system that can accommodate future enhancements, new features, and changes in the business requirements.

c. Potential Components and Tools:
- Front-end Development: HTML, CSS, JavaScript, and popular front-end frameworks like React or Vue.js for building the user interface.
- Back-end Development: Server-side languages like Python, Java, or Node.js, along with frameworks like Django, Spring Boot, or Express.js for handling business logic and data management.
- Database: Relational or NoSQL databases like MySQL, PostgreSQL, MongoDB, or Firebase for storing menu data, customer information, orders, and reservations.
- Payment Gateway: Integration with secure payment gateways such as Stripe, PayPal, or Braintree to handle payment transactions.
- Cloud Infrastructure: Utilizing cloud platforms like AWS, Azure, or Google Cloud for scalability, reliability, and hosting the application.
- Push Notifications: Utilizing services like Firebase Cloud Messaging or Apple Push Notification Service (APNs) to send real-time order status updates to customers.
- SMS/Email Integration: Integrating with SMS or email service providers to send order confirmations, updates, and promotional messages to customers.
- Loyalty Program Framework: Implementing a loyalty program framework or utilizing third-party solutions that enable the management and tracking of customer rewards and incentives.
- Delivery Service APIs: Integrating with delivery service APIs (e.g., Grubhub, Deliveroo) to streamline order placement, tracking, and delivery.


