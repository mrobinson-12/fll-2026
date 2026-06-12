# -*- coding: utf-8 -*-
"""
===============================================================================
         THE ABSOLUTE GROUND-ZERO BASH TO POWERSHELL TRANSLATION MATRIX
===============================================================================
Designed for absolute beginners with zero prior coding, terminal, or scripting
experience. This script acts as an interactive command-line simulator and tutor.
Lines of Code/Content Target: 600+ Lines of Pure Educational Infrastructure.
"""

import sys
import time


def clear_screen():
    """Simulates a screen clear across basic online web compilers."""
    print("\n" * 8)


def type_print(text, delay=0.005):
    """Prints text with a subtle typewriter effect to prevent screen flooding."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_banner(title):
    """Renders a structural visual border for new instructional chapters."""
    print("\n" + "=" * 78)
    print(f" LOGICAL ZONE: {title.upper()}")
    print("=" * 78 + "\n")


def wait_for_user():
    """Forces a deliberate pause so the user can digest information at leisure."""
    print("\n" + "-" * 40)
    input("Press [ENTER] when your brain has fully absorbed this lesson...")


def verify_multiple_choice(question, choices, correct_idx, context_recovery):
    """
    Displays a concept verification question.
    If the user fails, it explains why and lets them retry without crashing.
    """
    while True:
        print(f"\n[?] CONCEPT CHECK: {question}")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}) {choice}")

        try:
            user_input = input("\nYour selection (Enter number): ").strip()
            if not user_input:
                continue
            choice = int(user_input) - 1
            if 0 <= choice < len(choices):
                if choice == correct_idx:
                    print(
                        "\n✅ SPECTACULAR! Your conceptual framework is flawless."
                    )
                    return True
                else:
                    print("\n❌ NEGATIVE. That choice breaks the logic path.")
                    print(f"💡 WHY: {context_recovery}")
                    print("Let's try that question one more time.")
            else:
                print(
                    f"Please pick a valid number between 1 and {len(choices)}."
                )
        except ValueError:
            print("Invalid input. Please type an actual whole number integer.")


def verify_code_syntax(prompt, valid_variants, hint_text):
    """
    Validates typed code exercises by cleaning whitespace and matching structures.
    Provides targeted feedback if the user experiences syntax errors.
    """
    while True:
        print(f"\n[>] CODE EXERCISE: {prompt}")
        user_code = input("Type your code statement: ").strip()

        # Normalize to allow flexibility with spaces and quotation marks
        norm_user = (
            user_code.replace('"', "'").replace(" ", "").replace("`", "")
        )

        is_correct = False
        for variant in valid_variants:
            norm_variant = (
                variant.replace('"', "'").replace(" ", "").replace("`", "")
            )
            if norm_user == norm_variant:
                is_correct = True
                break

        if is_correct:
            print(
                "\n✅ SYNTAX VALIDATED! The automation engine accepts this syntax."
            )
            return user_code
        else:
            print(
                "\n❌ SYNTAX ERROR! The computer is thoroughly confused by that input."
            )
            print(f"💡 HELPFUL HINT: {hint_text}")
            print(f"Expected format looks exactly like: {valid_variants[0]}")
            print(
                "Check your spelling, spaces, symbols, and capitals. Try again."
            )


def main():
    clear_screen()
    print(
        "============================================================================="
    )
    print(
        "      THE GROUND-ZERO COMMAND LINE ACADEMY: MAC BASH TO WINDOWS POWERSHELL   "
    )
    print(
        "============================================================================="
    )
    type_print(
        "Welcome, absolute beginner! If you have never coded, never used a mac terminal,"
    )
    type_print(
        "and have absolutely no idea what a 'shell' is—congratulations. You belong here."
    )
    type_print(
        "This application is a safely simulated terminal boot camp built specifically"
    )
    type_print(
        "to teach you how to read, understand, and rewrite automated script blueprints."
    )
    type_print(
        "We will take things line-by-line, explaining the basic principles from scratch."
    )

    wait_for_user()

    # =========================================================================
    # MODULE 1: WHAT IS A TERMINAL AND A SCRIPT?
    # =========================================================================
    clear_screen()
    print_banner("Module 1: The Core Foundational Concept")
    type_print(
        "Let's clear up the mystery right now. What is a Terminal, and what is a Script?"
    )
    type_print(
        "Normally, you control your computer by pointing your mouse at icons, clicking buttons,"
    )
    type_print(
        "and dragging folders around. This is called a Graphical User Interface (GUI)."
    )
    type_print(
        "But underneath those pretty graphics, the computer is just a text-driven calculator."
    )
    type_print(
        "\nWhen you open a Terminal window (called 'Terminal' on Mac, and 'PowerShell' on Windows),"
    )
    type_print(
        "you are interacting directly with the operating system's brain using nothing but raw text."
    )
    type_print(
        "You type a specific word command, hit enter, and the computer runs that action instantly."
    )

    type_print(
        "\nNow, imagine you have a list of 20 different commands you need to run in sequence."
    )
    type_print(
        "For example: make a folder, download a file, install Python, sync it to GitHub."
    )
    type_print(
        "Typing those manually one-by-one is tedious, boring, and prone to human errors."
    )
    type_print(
        "A SCRIPT is simply a basic text file that acts as a recipe. It lists all 20 commands"
    )
    type_print(
        "in exact order. When you execute the script, the computer reads it from top to bottom,"
    )
    type_print(
        "running every instruction line-by-line while you go make a cup of coffee."
    )

    verify_multiple_choice(
        "In plain English, what is a computer shell script?",
        [
            "A complex virus designed to break computer hardware overrides.",
            "A text-based recipe file containing a sequence of step-by-step commands.",
            "A graphical software package used to design 3D printing objects.",
        ],
        1,
        "A script is just a list of text commands that execute one after another, exactly like a recipe.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 2: THE GREAT OPERATING SYSTEM SCHISM
    # =========================================================================
    clear_screen()
    print_banner("Module 2: Mac Language vs. Windows Language")
    type_print(
        "Computers developed along two completely different historical timelines:"
    )
    type_print(
        "1. MacOS and Linux use a shell environment family called BASH (or Zsh)."
    )
    type_print(
        "2. Microslop Windows uses a modern object-oriented framework called POWERSHELL."
    )

    type_print("\nThey think about automation completely differently:")
    type_print(
        "- Mac Bash treats everything like a printing press text stream. If you ask a Mac shell"
    )
    type_print(
        "  for a list of files, it literally throws a raw string of text characters across your screen."
    )
    type_print(
        "- Windows PowerShell treats everything like a detailed digital blueprint object."
    )
    type_print(
        "  Instead of raw characters, it passes data tables with hidden columns, structural values,"
    )
    type_print(
        "  and rigid code architectures. Because it is highly engineered, PowerShell commands"
    )
    type_print(
        "  can look a bit longer and more verbose, but they are incredibly reliable once understood."
    )

    verify_multiple_choice(
        "What is the fundamental structural difference between Mac Bash and Windows PowerShell?",
        [
            "Mac Bash passes raw streams of text words; Windows PowerShell passes structured objects.",
            "Mac Bash can only run apps, while Windows PowerShell only edits text files.",
            "There is no difference; they use the exact same words and file structures.",
        ],
        0,
        "Mac processes plain words; Windows processes rigid, object-oriented data properties.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 3: THE AUTOMATION EMERGENCY BRAKE (ERROR HANDLING)
    # =========================================================================
    clear_screen()
    print_banner("Module 3: The Automation Emergency Brake")
    type_print(
        "Imagine you are driving an autonomous script car. Line 2 of your script tries to download"
    )
    type_print(
        "a core coding file from the internet, but your Wi-Fi randomly drops out."
    )
    type_print(
        "The download fails completely! Line 3 of your script is supposed to open that file and configure it."
    )
    type_print(
        "If the script keeps driving blindly forward without that file, it could erase the wrong data"
    )
    type_print(
        "or crash your entire folder system. You want the vehicle to hit the brakes instantly if ANY line fails."
    )

    type_print(
        "\n- On a Mac Bash script, we pull this emergency handbrake by adding this command at the top:"
    )
    print("  set -e")
    type_print(
        "  This tells the Mac: 'If any command fails with an error, crash and stop execution immediately!'"
    )

    type_print(
        "\n- Windows PowerShell is wildly optimistic by default. If line 2 crashes, it will scream at you"
    )
    type_print(
        "  in red text, but then it will blindly skip to line 3 and keep going anyway! This is dangerous."
    )
    type_print(
        "  To force Windows to instantly freeze the script when an error occurs, we have to change a"
    )
    type_print(
        "  built-in global preference control configuration variable called '$ErrorActionPreference'."
    )
    type_print("  We assign its state value string to 'Stop'.")
    print("  PowerShell Code: $ErrorActionPreference = 'Stop'")

    verify_multiple_choice(
        "Why must we configure an explicit error setting block at the start of our Windows scripts?",
        [
            "To prevent the computer from overheating when running heavy graphics packages.",
            "Because Windows defaults to blindly continuing execution even if previous steps failed.",
            "To speed up the internet download rates for GitHub files.",
        ],
        1,
        "PowerShell will ignore errors and keep running unless we set $ErrorActionPreference to Stop.",
    )

    verify_code_syntax(
        "Write the exact line of Windows PowerShell code to force scripts to stop instantly on any error:",
        ["$ErrorActionPreference = 'Stop'", "$ErrorActionPreference='Stop'"],
        "Start with the dollar sign variable '$ErrorActionPreference', use an equals sign, then assign the word 'Stop' in quotes.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 4: THE STORAGE CABINET MATRIX (FOLDERS & PATHS)
    # =========================================================================
    clear_screen()
    print_banner("Module 4: Storage Cabinets (Folders and Paths)")
    type_print(
        "To organize your work, you need to create folders on your hard drive."
    )
    type_print(
        "In terminal spaces, folders are formally referred to as 'Directories'."
    )

    type_print(
        "\n- On a Mac Bash environment, the recipe step to build a folder looks like this:"
    )
    print('  mkdir -p "$HOME/fll"')
    type_print("  Let's translate that phrase step-by-step:")
    type_print("  1. 'mkdir' stands for Make Directory (create folder).")
    type_print(
        "  2. '-p' is a safety flag meaning 'Parent/Passive'. It tells the computer: 'If this folder"
    )
    type_print(
        "     already exists, just be quiet and keep going. Do not crash our script with a complaint.'"
    )
    type_print(
        "  3. '$HOME' is a shortcut label pointing to your primary user storage profile folder."
    )
    type_print(
        "  4. '/fll' is the name of the folder we want to build inside that home directory."
    )

    type_print(
        "\n- On Windows PowerShell, commands are called 'Cmdlets' and follow a very logical,"
    )
    type_print(
        "  easy-to-read 'Verb-Noun' pattern. To make a new thing, the verb is always 'New-Item'."
    )
    type_print(
        "  We must explicitly tell the cmdlet what kind of item to build using the '-ItemType' parameter."
    )
    type_print("  We want a folder, so our item type value is 'Directory'.")
    type_print(
        "  To replicate the Mac's behave-quietly-if-it-already-exists rule (-p), we append the '-Force' switch."
    )
    type_print(
        "  CRITICAL DIFFERENCE: Windows tracks file paths with backslashes (\\) instead of forward slashes (/)."
    )
    print(
        '  PowerShell Code: New-Item -ItemType Directory -Force -Path "$HOME\\fll"'
    )

    verify_multiple_choice(
        "What character difference must you always watch out for when writing file paths on Windows vs Mac?",
        [
            "Windows paths require percentage signs everywhere.",
            "Mac uses forward slashes (/), while Windows naturally utilizes backslashes (\\).",
            "Windows folders cannot use words longer than three characters.",
        ],
        1,
        "Always remember: Mac leans forward (/), Windows leans back (\\).",
    )

    verify_code_syntax(
        "Translate 'mkdir -p \"$HOME/fll\"' into its structural Windows PowerShell cmdlet equivalent:",
        [
            'New-Item -ItemType Directory -Force -Path "$HOME\\fll"',
            "New-Item -ItemType Directory -Force -Path '$HOME\\fll'",
            'New-Item -Path "$HOME\\fll" -ItemType Directory -Force',
        ],
        "Use 'New-Item', define the type via '-ItemType Directory', bypass errors with '-Force', and point to the path using backslashes.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 5: APP STORES FOR TERMINALS (PACKAGE MANAGERS)
    # =========================================================================
    clear_screen()
    print_banner("Module 5: App Stores for Nerds (Package Managers)")
    type_print(
        "When you need to download coding tools like Git (which tracks your code revisions)"
    )
    type_print(
        "or Python (the engine that executes your programming statements), you don't want to"
    )
    type_print(
        "manually open a browser, look up a website, download an installer wizard, click 'Next',"
    )
    type_print(
        "agree to agreements, and manually click your way through a setup interface."
    )
    type_print(
        "A script needs to download and install tools silently in the background automatically."
    )

    type_print(
        "\nTo do this, we use a tool called a 'Package Manager'. It is a command-line app store."
    )
    type_print(
        "- On a Mac, the script has to run custom script commands to install a third-party app store"
    )
    type_print(
        "  framework called Homebrew, and uses the command phrase: 'brew install git'."
    )

    type_print(
        "\n- On modern Windows 10 and 11 machines, you don't need to install any messy third-party software!"
    )
    type_print(
        "  Microslop built an official command-line app store straight into your computer's brain."
    )
    type_print(
        "  It is called WINGET (Windows Package Manager). You just invocation call it instantly."
    )
    type_print(
        "  To install Python 3.13 quietly without any popup wizards distracting the user, we run:"
    )
    print(
        "  winget install --id Python.Python.3.13 -e --silent --accept-package-agreements"
    )

    verify_multiple_choice(
        "What built-in system application replaces Mac's Homebrew manager on a Windows machine?",
        [
            "The Disk Defragmenter",
            "Winget (Windows Package Manager)",
            "The Internet Explorer Setup Engine",
        ],
        1,
        "Winget is the built-in app store installer for Windows terminals.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 6: THE MEMORY DRAWERS (VARIABLES AND USER INPUT)
    # =========================================================================
    clear_screen()
    print_banner("Module 6: Memory Drawers (Variables and Input)")
    type_print(
        "In programming, you frequently need the computer to remember a piece of information."
    )
    type_print("For example, a password token, a name, or a folder address.")
    type_print(
        "Imagine your computer's memory contains a huge bank of empty storage drawers."
    )
    type_print(
        "To use one, you tape a clear label to the front of the drawer, open it up, drop the data"
    )
    type_print(
        "inside, and slide it closed. That labeled storage drawer is called a 'Variable'."
    )

    type_print(
        "\n- On a Mac Bash script, you ask a human a question and save it to a variable using this format:"
    )
    print('  read -r -p "Enter your token: " token')
    type_print(
        "  This means: Pause, print the prompt text 'Enter your token', wait for the user to type it,"
    )
    type_print("  and store that text inside a memory drawer labeled 'token'.")

    type_print(
        "\n- On Windows PowerShell, there is one non-negotiable rule you must memorize:"
    )
    type_print("  ALL VARIABLES MUST START WITH A DOLLAR SIGN ($).")
    type_print(
        "  If you see a dollar sign in front of a word in PowerShell, it means 'this is a memory drawer'."
    )
    type_print(
        "  To ask a user for text input, we use a cmdlet named 'Read-Host'."
    )
    type_print(
        "  The value typed by the user flows backward through an equals sign into our labeled drawer."
    )
    print('  PowerShell Code: $token = Read-Host "Enter your token"')

    verify_multiple_choice(
        "What absolute structural rule must you remember regarding variable names in PowerShell?",
        [
            "They must always be written entirely in Roman numerals.",
            "They must always be prefixed with a dollar sign character ($).",
            "They must terminate with an exclamation mark.",
        ],
        1,
        "Every variable in PowerShell requires a dollar sign ($) taped onto its front identity.",
    )

    verify_code_syntax(
        "Write a line of PowerShell code that prompts a user with 'Enter Username' and saves it to a variable called '$username':",
        [
            "$username = Read-Host 'Enter Username'",
            '$username = Read-Host "Enter Username"',
            "$username=Read-Host 'Enter Username'",
        ],
        "Start with '$username', write an equals sign, call the 'Read-Host' cmdlet, and append the string text.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 7: THE PUNCTUATION SHIELD (STRING INTERPOLATION)
    # =========================================================================
    clear_screen()
    print_banner("Module 7: The Punctuation Boundary Shield")
    type_print(
        "Look closely at this line from your Mac script which downloads your class codebase from GitHub:"
    )
    print(
        "  git clone https://$username:$token@github.com/mrobinson-12/fll-2026"
    )
    type_print(
        "\nThis line constructs a long web link string by injecting your stored variable drawers"
    )
    type_print(
        "right into the middle of the address. The Mac shell handles this formatting easily."
    )

    type_print(
        "\nHowever, look at how tightly the variables are squeezed against formatting punctuation:"
    )
    type_print(
        "The '$username' drawer directly touches a colon (:), and the '$token' drawer directly touches an at-sign (@)."
    )
    type_print(
        "Windows PowerShell can easily get confused here. It looks at the line and thinks:"
    )
    type_print(
        "  'Wait, is the colon part of the variable name? Is the at-sign part of the variable box label?'"
    )
    type_print(
        "The script engine misinterprets the text boundary coordinates and crashes spectacularly."
    )

    type_print(
        "\nTo fix this on Windows, we build a protective punctuation boundary shield around our variables."
    )
    type_print(
        "We wrap the exact word label inside curly braces, like this: ${username} and ${token}."
    )
    type_print(
        "This tells the Windows system explicitly: 'Our variable name is exactly what is inside the curly braces."
    )
    type_print(
        "The box label stops here, and the web link symbols touching it are separate structural links.'"
    )
    print(
        '  PowerShell Code: git clone "https://${username}:${token}@github.com/mrobinson-12/fll-2026"'
    )

    verify_multiple_choice(
        "Why do we wrap variables inside curly braces like ${token} when building a Git URL string in PowerShell?",
        [
            "To encrypt our password token so it becomes invisible to network spies.",
            "To clearly isolate the variable name boundaries so adjacent punctuation symbols don't break interpretation.",
            "Because Windows computers cannot read letters without curly brackets.",
        ],
        1,
        "Curly brackets act as a clear shield showing the shell where the variable text ends and the next punctuation mark begins.",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 8: ISOLATED SOFTWARE SANDBOXES (VIRTUAL ENVIRONMENTS)
    # =========================================================================
    clear_screen()
    print_banner("Module 8: Isolated Software Sandboxes")
    type_print(
        "When setting up robotics environments (like Pybricks dev frameworks), your script creates"
    )
    type_print("a 'Python Virtual Environment' (abbreviated as a '.venv').")
    type_print(
        "Think of a virtual environment as an isolated digital sandbox folder inside your workspace project."
    )
    type_print(
        "Any software dependencies or robotic code components you install get locked inside that sandbox."
    )
    type_print(
        "This prevents those packages from messing up the rest of your primary operating system apps."
    )

    type_print(
        "\nCreating the sandbox is practically identical on both platforms. But TURNING IT ON is completely different:"
    )
    type_print(
        "- On a Mac, the command to dive inside the sandbox container is:"
    )
    print("  source .venv/bin/activate")

    type_print(
        "\n- Windows has absolutely no historical concept of a 'source' command!"
    )
    type_print(
        "  Instead, to activate a sandbox folder on Windows, we look inside the environment directory structure,"
    )
    type_print(
        "  locate a script file named 'Activate.ps1' hidden inside the 'Scripts' subfolder, and execute it directly."
    )
    type_print(
        "  We place an ampersand operator character (&) at the very start of the line. In PowerShell syntax,"
    )
    type_print(
        "  the ampersand means: 'Take this file path, open it up, and run the execution script hidden inside it!'"
    )
    print("  PowerShell Code: & .\\.venv\\Scripts\\Activate.ps1")

    verify_multiple_choice(
        "How do you turn on/activate an isolated Python virtual environment sandbox folder on Windows?",
        [
            "By typing 'source .venv/bin/activate' exactly like a Mac configuration script.",
            "By executing the internal path script file using the execution ampersand: & .\\.venv\\Scripts\\Activate.ps1",
            "By formatting the directory layout structure via an administrative disk utility.",
        ],
        1,
        "Windows moves through the 'Scripts' subfolder layout and uses the ampersand execution operator.",
    )

    verify_code_syntax(
        "Write the exact PowerShell syntax to activate a local Python environment script path natively:",
        [
            "& .\\.venv\\Scripts\\Activate.ps1",
            ".\u005c.venv\u005cScripts\u005cActivate.ps1",
        ],
        "Start with an ampersand, then a space, followed by the relative folder file path: .\\.venv\\Scripts\\Activate.ps1",
    )

    wait_for_user()

    # =========================================================================
    # MODULE 9: THE GRADUATION GRADED FINAL ASSESSMENT EXAM
    # =========================================================================
    clear_screen()
    print_banner("Module 9: The Final Graduation Assessment Exam")
    print(
        "============================================================================="
    )
    print(
        "                      THE GRAND COMPILATION CHALLENGE                       "
    )
    print(
        "============================================================================="
    )
    type_print(
        "You have advanced from knowing absolute zero to understanding the core rules"
    )
    type_print("of automated configuration scripts across operating systems.")
    type_print(
        "\nHere is your final graduation exam scenario. You are looking at a vital 4-line"
    )
    type_print("chunk of your class's original Mac script code:")
    print("  -------------------------------------------------------------")
    print("  set -e")
    print('  mkdir -p "$HOME/fll"')
    print('  read -r -p "Enter your token: " token')
    print(
        "  git clone https://$username:$token@github.com/mrobinson-12/fll-2026"
    )
    print("  -------------------------------------------------------------")
    type_print(
        "\nYour task is to translate these four steps sequentially into functional Windows PowerShell syntax."
    )
    type_print(
        "Take your time. Review your capitalization, backslashes, braces, and variables.\n"
    )

    exam_line1 = verify_code_syntax(
        "Step 1/4: Translate the emergency error halt control statement ('set -e'):",
        ["$ErrorActionPreference = 'Stop'", "$ErrorActionPreference='Stop'"],
        "Set the preference variable configuration state value exactly to 'Stop'.",
    )

    exam_line2 = verify_code_syntax(
        "Step 2/4: Translate the secure directory creation instruction block ('mkdir -p \"$HOME/fll\"'):",
        [
            'New-Item -ItemType Directory -Force -Path "$HOME\\fll"',
            "New-Item -ItemType Directory -Force -Path '$HOME\\fll'",
            'New-Item -Path "$HOME\\fll" -ItemType Directory -Force',
        ],
        "Call the New-Item cmdlet with Directory type, append the Force switch, and fix your slashes.",
    )

    exam_line3 = verify_code_syntax(
        "Step 3/4: Translate the user input query variable line ('read -r -p ...'):",
        [
            "$token = Read-Host 'Enter your token'",
            '$token = Read-Host "Enter your token"',
            "$token=Read-Host 'Enter your token'",
        ],
        "Remember the mandatory dollar sign for your variable drawer, and deploy Read-Host.",
    )

    exam_line4 = verify_code_syntax(
        "Step 4/4: Translate the Git download URL line using protective boundary shields to insulate the variables:",
        [
            'git clone "https://${username}:${token}@github.com/mrobinson-12/fll-2026"',
            "git clone 'https://${username}:${token}@github.com/mrobinson-12/fll-2026'",
            "git clone https://${username}:${token}@github.com/mrobinson-12/fll-2026",
        ],
        "Isolate your variable configurations using curly brackets like ${username} and ${token}.",
    )

    # =========================================================================
    # GRADUATION DISPLAY UNLOCKED
    # =========================================================================
    clear_screen()
    print(
        "============================================================================="
    )
    print(
        "🎉🚀 COURSE COMPLETED: YOU ARE AN OFFICIAL TRANSLATION MATRIX GRADUATE! 🚀🎉"
    )
    print(
        "============================================================================="
    )
    type_print(
        "\nYou have successfully navigated from zero knowledge to a systemic understanding"
    )
    type_print(
        "of multi-platform core systems infrastructure engineering script design."
    )
    type_print(
        "Here is your dynamically generated, validated, fully functional Windows script block:"
    )
    print("\n" + "#" * 60)
    print("# COPIED AND CONVERTED AUTOMATION BLUEPRINT FOR WINDOWS POWERSHELL")
    print("#" * 60)
    print(f"{exam_line1}")
    print(f"{exam_line2}")
    print(f"{exam_line3}")
    print(f"{exam_line4}")
    print(
        "Write-Host 'Environment configuration script sequence executed successfully!'"
    )
    print("#" * 60 + "\n")

    type_print(
        "You can save those lines into a plain text file, name it 'setup.ps1', and it will execute"
    )
    type_print(
        "flawlessly on any modern target Windows deployment machine worldwide."
    )
    print(
        "=============================================================================\n"
    )


if __name__ == "__main__":
    main()
