from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

from datetime import datetime
import subprocess

# from django.shortcuts import render
from .models import problem, testcase  # Import your 'Problem' model from models.py

def HomePage(request):
    probs = problem.objects.all()
    return render(request, 'home.html', {'probs': probs})

def problem_description(request, problem_id):
    # Assuming you have a 'problem_id' parameter to fetch the specific problem
    prob = problem.objects.get(pk=problem_id)
    # print(prob)
    return render(request, 'description.html', {'prob': prob})

# def submit_code(request, problem_id):
#     code=request.POST["code"]
#     prob = problem.objects.get(pk=problem_id)
#     # print(prob.id)
#     language=request.POST["language"]
#     prob_id = prob.id
#     prob_name = prob.name
#     curr_time = datetime.now()
#     curr_lang = ""

#     if language == "cpp":
#         file_path = "assets/ compile1.cpp"
#         tc = testcase.objects.get(pk = problem_id)

#         # run_cppfile()

#     return render(request, 'verdict.html', {'prob': prob})
import os

# ... Other imports and views ...

def submit_code(request, problem_id):
    code = request.POST.get("code", "")
    prob = problem.objects.get(pk=problem_id)
    language = request.POST.get("language", "")
    prob_id = prob.id
    prob_name = prob.name
    curr_time = datetime.now()
    curr_lang = ""

    if language == "cpp":
        file_path = "assets/compile1.cpp"

        # Write the code to the compile1.cpp file in the assets folder.
        with open(file_path, 'w') as cpp_file:
            cpp_file.write(code)

        # Check if the file exists before attempting to compile.
        if os.path.exists(file_path):
            # Use 'question_id' to filter test cases related to the problem.
            testcases = testcase.objects.filter(question_id=problem_id)

            # Create a list of test cases to pass to the run_cppfile function.
            input_data = [{'input': tc.test, 'result': tc.result} for tc in testcases]

            # Run the code for all test cases and get the verdict and test results.
            verdict, test_results = run_cppfile(input_data, code)

            # Display the verdict and test results on the verdict.html template.
            return render(request, 'verdict.html', {'prob': prob, 'verdict': verdict, 'test_results': test_results})
        else:
            # Handle the case where the file doesn't exist.
            return HttpResponse("Failed to write code to compile1.cpp")
    elif language == "java":
        # Use 'question_id' to filter test cases related to the problem.
        testcases = testcase.objects.filter(question_id=problem_id)

        # Create a list of test cases to pass to the run_javafile function.
        input_data = [{'input': tc.test, 'result': tc.result} for tc in testcases]

        # Run the Java code and get the verdict and test results.
        verdict, test_results = run_javafile(input_data, code)

    elif language == "python":
        # Use 'question_id' to filter test cases related to the problem.
        testcases = testcase.objects.filter(question_id=problem_id)

        # Create a list of test cases to pass to the run_pythonfile function.
        input_data = [{'input': tc.test, 'result': tc.result} for tc in testcases]

        # Run the Python code and get the verdict and test results.
        verdict, test_results = run_pythonfile(input_data, code)

    else:
        # Handle other languages here if needed.
        return HttpResponse("Unsupported Language")

    # Display the verdict and test results on the verdict.html template.
    return render(request, 'verdict.html', {'prob': prob, 'verdict': verdict, 'test_results': test_results})

def run_cppfile(input_data, code):
    # Write the code to the compile1.cpp file in the assets folder.
    with open('assets/compile1.cpp', 'w') as cpp_file:
        cpp_file.write(code)

    # Check if the file exists before attempting to compile.
    if os.path.exists('assets/compile1.cpp'):
        try:
            compiled_output = subprocess.check_output(['g++', '-o', 'assets/compiled', 'assets/compile1.cpp'], stderr=subprocess.STDOUT, timeout=5, text=True)
            if compiled_output:
                return "Compilation Error", []

            # Run the compiled code with each test case input.
            test_results = []
            for testcase in input_data:
                try:
                    output = subprocess.check_output(['./assets/compiled'], stderr=subprocess.STDOUT, timeout=5, input=testcase['input'], text=True)
                    output = output.strip()

                    # Compare the output with the expected result for the test case.
                    if output == testcase['result']:
                        test_results.append("Accepted")
                    else:
                        test_results.append("Wrong Answer")
                except subprocess.TimeoutExpired:
                    test_results.append("Time Limit Exceeded")
                except subprocess.CalledProcessError as e:
                    test_results.append(e.output.strip())

            return "Accepted" if all(result == "Accepted" for result in test_results) else "Wrong Answer", test_results
        except subprocess.CalledProcessError as e:
            return "Compilation Error", [e.output.strip()]
    else:
        # Handle the case where the file doesn't exist.
        return "Failed to write code to compile1.cpp", []


def run_javafile(input_data, code):
    # Write the code to the compile1.java file in the assets folder.
    with open('assets/compile1.java', 'w') as java_file:
        java_file.write(code)

    # Check if the file exists before attempting to compile.
    if os.path.exists('assets/compile1.java'):
        try:
            # Compile the Java code.
            compiled_output = subprocess.check_output(['java', 'assets/compile1.java'], stderr=subprocess.STDOUT, timeout=5, text=True)
            if compiled_output:
                return "Compilation Error", []

            # Get the class name (assuming it's the same as the filename without the .java extension).
            class_name = os.path.splitext(os.path.basename('assets/compile1.java'))[0]

            # Run the compiled Java code with each test case input.
            test_results = []
            for testcase in input_data:
                try:
                    output = subprocess.check_output(['javac', class_name], stderr=subprocess.STDOUT, timeout=5, input=testcase['input'], text=True)
                    output = output.strip()

                    # Compare the output with the expected result for the test case.
                    if output == testcase['result']:
                        test_results.append("Accepted")
                    else:
                        test_results.append("Wrong Answer")
                except subprocess.TimeoutExpired:
                    test_results.append("Time Limit Exceeded")
                except subprocess.CalledProcessError as e:
                    test_results.append(e.output.strip())

            return "Accepted" if all(result == "Accepted" for result in test_results) else "Wrong Answer", test_results
        except subprocess.CalledProcessError as e:
            return "Compilation Error", [e.output.strip()]
    else:
        # Handle the case where the file doesn't exist.
        return "Failed to write code to compile1.java", []

import sys

def run_pythonfile(input_data, code):
    # Write the code to the compile1.py file in the assets folder.
    with open('assets/compile2.py', 'w') as python_file:
        python_file.write(code)

    # Check if the file exists before attempting to run.
    if os.path.exists('assets/compile2.py'):
        try:
            # Run the Python code with each test case input.
            test_results = []
            for testcase in input_data:
                try:
                    # Split the input string into individual numbers.
                    num1, num2 = map(int, testcase['input'].strip().split())

                    # Execute the Python script and capture the output.
                    output = subprocess.check_output(
                        ['python', 'assets/compile2.py'],
                        stderr=subprocess.STDOUT,
                        timeout=5,
                        input=f"{num1}\n{num2}\n",
                        text=True
                    )

                    output = output.strip()

                    # Compare the output with the expected result for the test case.
                    if output == testcase['result']:
                        test_results.append("Accepted")
                    else:
                        test_results.append("Wrong Answer")
                except subprocess.TimeoutExpired:
                    test_results.append("Time Limit Exceeded")
                except subprocess.CalledProcessError as e:
                    test_results.append(e.output.strip())

            return "Accepted" if all(result == "Accepted" for result in test_results) else "Wrong Answer", test_results
        except subprocess.CalledProcessError as e:
            return "Execution Error", [e.output.strip()]
    else:
        # Handle the case where the file doesn't exist.
        return "Failed to write code to compile2.py", []
