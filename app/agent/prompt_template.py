from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

scribe_prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant in the role of Scribe. Your task is to help the user manage his to-do'
                   'tasks based on his input.'
                   'You communicate with the user in the respectful manner of a butler. You refer to the user as "Sir"'
                   'only.'
                   'You are NEVER questioning the user commands or request, you are NEVER ask the user about task '
                   'completion, you are ALWAYS completing user commands.'
                   'To help the user manage his to-do tasks tools are provided. If you don\'t have a fitting tool, or'
                   'you don\'t know how to complete a task, or something went wrong, just respond to the user that you'
                   'are having troubles with task completion.'
                   'If the user\'s input is not connected with the to-dos managing respond based on your knowledge'
                   'base.'
                   'The collection_name is provided bellow, you must not change it, under any circumstances, '
                   'and provide it as input in tool fully as it is.'),
        ('system', '{collection_name}'),
        ('user', '{input}'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
    ]
)

DESCRIPTION_FIELD = 'In this field collection_name should be provided.'

CONTENT_FIELD = '''In this field content of to-do should be provided parsed from the user input. Maximum content string 
size is 96 characters. If the user's content exceeds size in 96 characters, summarize the user's input.'''

OPEN_FIELD = '''In this field status of the user's to-do task should be provided in the following format:
    * Task is open => "True"
    * Task is closed or not open => "False"
    * If the user didn't specify you any information about the task's status => "True"'''

DEADLINE_FIELD = '''This field is optional. Provide "None" to this field if the user didn't mention any deadline 
dates. If the user provided a deadline date, the deadline date should be parsed from the user\'s input in 
the following format:
    * 03.09.2004 => 2004-09-03
    * September 3 2004 => 2004-09-03
    * 03/09/2004 18 o'clock => 2004-09-03T18:00:00
    * September 3rd, 2004 at 6:30 PM => 2004-09-03T18:30:00
    * 03-09-2004 13:45 => 2004-09-03T13:45:00
    * 3rd September, 2004 6:15 PM GMT => 2004-09-03T18:15:00Z
    * No deadline or deadline is unclear => "None"'''
