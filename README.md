# DPO
Welcome to the DPO repository. 
This project helps to automate the filling of binding statement DPO (**Záväzné vyjadrenie DPO**) for **Západoslovenská distibučná a.s.** company.

## Disclaimer
- Information and error messages are written in Slovak, as this is more convenient for the users of this product.
- I am **not** affiliated with *Západoslovenská distibučná a.s.* in any way. This project was created for my father, who works there, to help automate part of his workflow.
- The file `parser.py` parsing the structured request data from `.xml` file is **not** included. (I am not sure whether the `.xml` structure is confidential or not).
This means that newly cloned project will **not** work because it uses functionality written in this file.

I will add a **dummy** `parser.py` in the repo in the future.

## Requirements
1. Firstly, please install dependencies:
```
pip install -r requirements.txt
```
2. The `.xml` file named `šišan.xml` is required as a structuted request data which are then parsed. This exact request (including naming of the `.xml` file) is required by the customer.
3. The file `VZOR - Záväzné vyjadrenie DPO.docx` serves as a **template** from which program generates binding statements.

These files are **not** added to this repo for security reasons.
The file `parser.py` parsing the structured request data is **not** included too.

## Usage
To run the project, use:

```
python3 main.py
```

## Output
The program creates two new files:
- `log_{success}_{time_stamp}.txt` - informs user about success / failure of the script
- `{Project.id} - DPO ({timestamp}).docx` - the generated binding statement


## Project status
The project is currently functional (see the `master` branch).

## Planned work and extensions
1. Extension of a GUI (see the `development` branch).
2. Preparation of full project documentation.
