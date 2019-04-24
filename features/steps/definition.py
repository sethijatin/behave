from behave import *

@step('A random precondition for the scenario')
def randomStepImplementation(context):
    context.vars = "Hello World"

@step('An action designated by the user using free style text')
def randomStepTwo(context):
    print(context.vars)
    print(context.text)

@step('The desired behavior is expected in the system')
def randomStepThree(context):
    pass
