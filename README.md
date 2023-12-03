# Home Security Bot

The Home Security Bot Project was developed as part of the software engineering module at the University College Cork (UCC)

The project's purpose is to demonstrate various aspects of software engineering, including system design and testing.

The project addresses the problem of traditional home security systems, which often rely on outdated technology and provide reactive security measures. These systems may only alert homeowners or authorities after a security breach has occurred, leading to delays in response and potential security risks.

To solve this problem, the project introduces the concept of a "Home Security Bot." This bot is designed to be an innovative and proactive security system for homes.

# How to install

## Windows

1. Extract zip folder
2. Open Powershell (make sure you are in the project directory)
3. Ensure you are running with the correct permissions

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

4. Ensure you have python installed

```bash
python --version
```

5. Create a virtual environment

```bash
python -m venv venv
```

6. Activate the virtual environment

```bash
.\venv\Scripts\Activate
```

7. Install dependancies

```bash
pip install -r requirements.txt
```

8. Run the program (ensure you are in the root of the folder)

```bash
python main.py
```

## Mac/Linux

1. Extract zip folder
2. Open Terminal
3. Ensure you have python installed

```bash
python --version
```

4. Create a virtual environment

```bash
python -m venv venv
```

5. Activate the virtual environment

```bash
source venv/bin/activate
```

6. Install dependancies

```bash
python -m install requirements.txt
```

7. Run the program (ensure you are in the root of the folder)

```bash
python main.py
```

# Testing

1. To run the testing suite

```bash
pytest
```

2. To run the testing suite with branch coverage

```bash
pytest --cov
```

3. To run the mutation tests

```bash
mut.py --target file_name --unit-test test --runner pytest
```
