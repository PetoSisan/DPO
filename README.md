# DPO
Welcome to the DPO repository. 
Thi project helps to automate the filling of binding statement DPO (**Záväzné vyjadrenie DPO**) for **Západoslovenská distibučná a.s.** company.

## Requirements
1. The `.xml` file named `šišan.xml` is required as a structuted request data which are then parsed. This request is required by Project sponsor.
2. The file `VZOR - Záväzné vyjadrenie DPO.docx` serves as a **template** from which program generates binding statements.

These files are **not** added to this repo for security reasons.

## Usage
To run the project, use:

```
python3 main.py
```

## Output
Program creates two new files:
- `log_{time_stamp}.txt` - informs user about success / failure of the script
- `Záväzné vyjadrenie DPO {applicant.get_full_name()} ({timestamp}).docx` - the generated binding statement


## Project status
Project is currently **under development**.