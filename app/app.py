Here is an example of Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for loan applications
loan_applications = []

@app.route('/loan_application', methods=['POST'])
def create_loan_application():
    data = request.get_json()
    applicant_id = data.get('applicant_id')
    
    # Check if the applicant already has an active loan application
    for application in loan_applications:
        if application['applicant_id'] == applicant_id and application['status'] == 'active':
            return jsonify({'message': 'Duplicate loan application not allowed'}), 400
    
    # Create a new loan application
    loan_application = {
        'applicant_id': applicant_id,
        'status': 'active',
        'details': data.get('details')
    }
    loan_applications.append(loan_application)
    
    return jsonify({'message': 'Loan application created successfully'}), 201

@app.route('/loan_applications/<applicant_id>', methods=['GET'])
def get_loan_applications(applicant_id):
    # Get all loan applications associated with the applicant
    applications = [application for application in loan_applications if application['applicant_id'] == applicant_id]
    
    return jsonify(applications), 200

@app.route('/loan_application/<application_id>', methods=['PUT'])
def update_loan_application(application_id):
    data = request.get_json()
    
    # Find the loan application by ID
    for application in loan_applications:
        if application['id'] == application_id:
            application['status'] = data.get('status')
            application['details'] = data.get('details')
            return jsonify({'message': 'Loan application updated successfully'}), 200
    
    return jsonify({'message': 'Loan application not found'}), 404

if __name__ == '__main__':
    app.run()
```

This code defines three API endpoints:
1. `/loan_application` - POST endpoint to create a new loan application. It checks if the applicant already has an active loan application and prevents duplicates.
2. `/loan_applications/<applicant_id>` - GET endpoint to retrieve all loan applications associated with a single applicant.
3. `/loan_application/<application_id>` - PUT endpoint to update a loan application's status and details.

You can run this Flask API code by executing the script. The API will be accessible at `http://localhost:5000`. Please note that this is a simplified example and does not include database integration or authentication/authorization mechanisms.