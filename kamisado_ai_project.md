# 2BA AI Project Review - Kamisado

[https://github.com/Giff21/Projet-Kamisado](https://github.com/Giff21/Projet-Kamisado)

## Git usage

- merge, rebase, PR, 1 branch = 1 feature & person

## Github repo

- Always add license to public repo ([https://choosealicense.com](https://choosealicense.com)): MIT 99% of the time
- Use [GitHub default Python .gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
- Add depedencies to requirements.txt

## Project structure

- Place all code in `src` or `kamisado` (project name) folder or similar + `tests` folder to separate code from tests and other general files
- Avoid duplicating all files `Pawn_finder.py`/`Pawn_finder2.py`, `Server_connect.py`/`ServerCommunication.py`/`communication.py`.
- Keep code inside a file relevent to the file name. `Move` and `FindPawn` are game related logic and should not be in `Server_connect.py` (which should only contain code related to server connection).

## Code quality

_2 points on evaluation grid !_

1. Best practice is to use [**PEP 8**](https://peps.python.org/pep-0008/) for all Python code guidelines & conventions.
    - Naming conventions (the most important is to be consistent across the whole codebase): **important**

        ```python
        CONSTANT_NAME = 1 # Constants in uppercase

        variable_name = 1 # Variables in snake_case

        def function_name(): # Functions in snake_case

        class ClassName: # Classes in PascalCase
        ```

    - Identation, line length, spacing, imports: **use [Ruff](https://docs.astral.sh/ruff/) !** The leader formatter & linter for Python -> Install [Ruff VSCode extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

        Always have these settings for better Python development, so you do not have to manually run formatting. Default formatter can be set to Ruff if you want to use it.

        ```json
        // settings.json
        {
            // Other settings...

            "[python]": {
                "editor.codeActionsOnSave": {
                    "source.organizeImports": "explicit"
                },
                "editor.defaultFormatter": "charliermarsh.ruff",
                "editor.formatOnSave": true,
                "editor.wordWrap": "on"
            }

            // Other settings...
        }
        ```

2. **Add comments in code !!** In particular for complex logic and non-obvious code. Write them for others, yourself to remember, and for the teacher that will rapidly look at it.

3. Add docstrings to all functions and classes. It helps a lot for readability and understanding the code & parameters. VSCode will also show this documentation when trying to use the function or class.
    - **Use [autoDocstring VSCode extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)** (can configure the style in VSCode settings `autoDocstring.docstringFormat`)

4. Try to use type hints for function parameters and return types as much as possible. It will not throw errors if you use the wrong type, but it will help a lot to understand the code and to avoid mistakes early. VSCode will also propose functions based on parameter types.

5. Avoid hardcoding values in the code, use variables, constants or **Enumerations** (restriction to a set of constants) instead (especially for strings). If a value will be reused multiple times, use them.

    ```python
    from enum import IntEnum, StrEnum # Enum for general enumerations

    class Play(StrEnum):
        FORWARD = 'forward'
        RDIAGONAL = 'Rdiagonal'
        LDIAGONAL = 'Ldiagonal'

    class CurrentPlayer(IntEnum):
        PLAYER_1 = 0
        PLAYER_2 = 1

    # Avoid typos, duplication of strings, and restricts the expected values to these ones
    ```

    Will go from this:

    ```python
    # Server_connect.py
    def Move(JEF_towerPosition : list, JEF_currentInStateJson : int, play : str):

        # Not clear what is in JEF_towerPosition and currentPosition
        currentPosition = [JEF_towerPosition[0], JEF_towerPosition[1]]

        if JEF_currentInStateJson == 0:
            if play == 'forward':
                finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]]
            if play == 'Rdiagonal':
                finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]+random.randint(0,currentPosition[1])]
            if play == 'Ldiagonal':
                finalPosition = [currentPosition[0]-random.randint(0,currentPosition[0]), currentPosition[1]-random.randint(0,currentPosition[1])]

            if  currentPosition[0] == finalPosition[0] or currentPosition[1] == finalPosition[1]:
                finalPosition = [finalPosition[0]-1, finalPosition[1]]

        elif JEF_currentInStateJson == 1:
            if play == 'forward':
                finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]]
            if play == 'Rdiagonal':
                finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]-random.randint(0,7-currentPosition[1])]
            if play == 'Ldiagonal':
                finalPosition = [currentPosition[0]+random.randint(0,7-currentPosition[0]), currentPosition[1]+random.randint(0,7-currentPosition[1])]

            if currentPosition[0] == finalPosition[0] or currentPosition[1] == finalPosition[1]:
                finalPosition = [finalPosition[0]+1, finalPosition[1]+1]

        print(play,":",currentPosition,",",finalPosition) # Way easier with f-strings
        return currentPosition, finalPosition
    ```

    To this:

    ```python
    # Best would be:
    # def Move(dark_pawn_pos : list, light_pawn_pos : list, current_player : CurrentPlayer, play : Play) -> tuple:
    def Move(JEF_towerPosition : list[list], JEF_currentInStateJson : int, play : str) -> tuple:

        # currentPosition = [JEF_towerPosition[0], JEF_towerPosition[1]]
        # (Best is to pass each pawn pos as a parameter)
        dark_pawn_pos, light_pawn_pos = JEF_towerPosition[0:2]

        if JEF_currentInStateJson == CurrentPlayer.PLAYER_1:
            if play == Play.FORWARD:
                finalPosition = [dark_pawn_pos - random.randint(0, dark_pawn_pos), light_pawn_pos]
            if play == Play.RDIAGONAL:
                finalPosition = [dark_pawn_pos - random.randint(0, dark_pawn_pos), light_pawn_pos + random.randint(0, light_pawn_pos)]
            if play == Play.LDIAGONAL:
                finalPosition = [dark_pawn_pos - random.randint(0, dark_pawn_pos), light_pawn_pos - random.randint(0, light_pawn_pos)]

            if  dark_pawn_pos == finalPosition[0] or light_pawn_pos == finalPosition[1]:
                finalPosition = [finalPosition[0] - 1, finalPosition[1]]

        elif JEF_currentInStateJson == CurrentPlayer.PLAYER_2:
            if play == Play.FORWARD:
                finalPosition = [dark_pawn_pos + random.randint(0, 7 - dark_pawn_pos), light_pawn_pos]
            if play == Play.RDIAGONAL:
                finalPosition = [dark_pawn_pos + random.randint(0, 7 - dark_pawn_pos), light_pawn_pos - random.randint(0, 7 - light_pawn_pos)]
            if play == Play.LDIAGONAL:
                finalPosition = [dark_pawn_pos + random.randint(0, 7 - dark_pawn_pos), light_pawn_pos + random.randint(0, 7 - light_pawn_pos)]

            if dark_pawn_pos == finalPosition[0] or light_pawn_pos == finalPosition[1]:
                finalPosition = [finalPosition[0] + 1, finalPosition[1] + 1]

        print(f"{play} : current = {[dark_pawn_pos, light_pawn_pos]}, final = {finalPosition}")
        return [dark_pawn_pos, light_pawn_pos], finalPosition

    Move(tower_pos, 0, "forward")
    # Or
    Move(tower_pos, CurrentPlayer.PLAYER_1, Play.FORWARD)
    ```

6. Give meaningful names to variables, functions, classes, and parameters.

    ```python
    for i in range(8):
         for j in range(8):
             case = iniState[i][j][1]

    # If it is the board state, 'row' & 'col' make it more understandable
     for row in range(BOARD_SIZE):
         for col in range(BOARD_SIZE):
             case = iniState[row][col][1]
             # Do something with case

    ```

## Testing

The codebase will need to be tested with `pytest` unit tests.

> Vos tests couvrent plus de 50% de votre code: **1**
>
> Vos tests couvrent plus de 80% de votre code: **1**

The easiest way to test a function is to have the function do only one specific thing.
For example, having 1 function handling all server related code will make it very hard to test every possible case.

Decompose complex functions into smaller ones, and put similar/duplicate code in a function that can be reused.

Also make sure functions do not return complex data structures like lists of dicts etc, which makes it harder to test (except for some like the board state).
Often, `list[dict[str, dict]]` means that the function is doing too much and should be decomposed into smaller ones.

Add tests status badge to the README.md file (as explained on [his website](https://quentin.lurkin.xyz/courses/python2be/course12/#slide-1)) to automatically see if tests are passing at each commit.
You can also use the awesome [Codecov](https://docs.codecov.com/docs/quick-start) to automatically run tests and get code coverage at each commit and displayed with a nice README.md badge.
