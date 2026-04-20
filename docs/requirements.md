# Functional requirements
1. The system will extract relevant project data from a file `šišan.xml`.
2. The system will offer a possibility to fill a form in **GUI** for obtaining statement from reviewer of a presented project.
3. The system will then create `{Project.id} - DPO ({timestamp}).docx` (generated DPO binding statement) based on the template `VZOR - Záväzné vyjadrenie DPO.docx` from hoarded data.
4. The system will **log** its success / failure to `log_{success}_{time_stamp}.txt` file.

# Nonfunctional requirements
1. Logic of app will be implemented in **Python**.
2. GUI will be implemented using **Qt for Python** framework.
3. The whole process of extracting data and creating the final statement (excluding interaction with a user) should take less than 1 sec.