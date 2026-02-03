# DPO
Welcome to the DPO repository. 
This project helps to automate the filling of binding statement DPO (**Záväzné vyjadrenie DPO**) for **Západoslovenská distibučná a.s.** company.

## Disclaimer
- Information and error messages are written in Slovak, as this is more convenient for the users of this product.
- I am **not** affiliated with *Západoslovenská distibučná a.s.* in any way. This project was created for my father, who works there, to help automate part of his workflow.

## Requirements
1. The `.xml` file named `šišan.xml` is required as a structuted request data which are then parsed. This exact request (including naming of the `.xml` file) is required by Project owner.
2. The file `VZOR - Záväzné vyjadrenie DPO.docx` serves as a **template** from which program generates binding statements.

These files are **not** added to this repo for security reasons.
The file `parser.py` parsing the structured request data is **not** included too.

3. As next step, please install dependencies:
```
pip install -r requirements.txt
```

## Usage
To run the project, use:

```
python3 main.py
```

## Output
Program creates two new files:
- `log_{success}_{time_stamp}.txt` - informs user about success / failure of the script
- `{Project.id} - DPO ({timestamp}).docx` - the generated binding statement


## Project status
Project is currently working but there is still a lot space for improvements:
1. There is still need to **write a documentation**.
2. There is a possibility to create a GUI extension which needs to be firstly discussed with project owner.