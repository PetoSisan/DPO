# Functional requirements

## General
1. The whole UI will be written in **Slovak**.
2. The system will offer a processing of the multiple `.xml` files from a **chosen directory** in one execution of the program.

## Extracting data
1. The system will extract relevant project data from a file `šišan.xml`.

## Form
1. The system will offer a possibility to fill out a form in a **GUI** for obtaining statement from **electrical connection technician**.
2. The system will support single and multiple choice questions in the form.
3. The system will offer traversing the form via buttons `Previous` and  `Next` (or maybe better said their localized variants `Predošlá otázka` and `Nasledujúca otázka`)
4. The system will show at the end of the form the **summary** of technician's answers.
5. The chosen answers will be writen into the second part of the resulted binding statement (see `Output 1.`).


## Output
1. The system will create `{Project.id} - DPO ({timestamp}).docx` (generated DPO binding statement) based on the template `VZOR - Záväzné vyjadrenie DPO.docx` from a hoarded data (`.xml` file + form if it was not skipped).
2. The system will **log** execution of the program to `log_{success}_{time_stamp}.txt` file indicating **success** / **fail** of the program.

## Sending as a attachment
1. The technician will have a possibibity to send generated statement via mail as a attachment to his **supervisor** for a **review**. 
This requirement has a low priority - perhaps in the later stage of the project.


# Nonfunctional requirements
1. Logic of the app will be implemented in **Python**.
2. GUI will be implemented using **Qt for Python** framework.
3. The whole process of extracting data and creating the final statement (excluding interaction with a user) should take less than 1 sec.