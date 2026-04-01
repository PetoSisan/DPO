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
1. The `.xml` file named `šišan.xml` is required as a structuted request data. This exaxt name of the `.xml` file is required by the customer.
2. The file `VZOR - Záväzné vyjadrenie DPO.docx` serves as a **template** from which program generates binding statements.

These files are **not** added to this repo. I will add these **dummy** files in the repo in the future.

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
Project is currently working (or maybe better said see **requirements**)

## Planned extensions
1. There is still need to **write a documentation**.
2. There is a possibility to create a GUI extension which needs to be firstly discussed with the customer. (see a `development` branch)