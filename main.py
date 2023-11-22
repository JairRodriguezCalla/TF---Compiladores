import os
import sys
import pickle

# Códigos ANSI para colores
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

def run_command(command, variables):
    try:
        os.system(command)
    except Exception as e:
        print(f"{Colors.RED}Error al ejecutar el comando: {e}{Colors.RESET}")

def parse_if_statement(statement, variables):
    parts = statement.split()
    if len(parts) >= 4 and parts[0] == "if" and parts[-1] == "then":
        condition = " ".join(parts[1:-1])
        for var_name, var_value in variables.items():
            condition = condition.replace(var_name, str(var_value))
        return condition
    else:
        return None

def parse_switch_statement(statement, variables):
    parts = statement.split()
    if len(parts) >= 4 and parts[0] == "switch" and parts[2] == "case":
        switch_expr = parts[1]
        for var_name, var_value in variables.items():
            switch_expr = switch_expr.replace(var_name, str(var_value))
        
        case_expr = parts[3]
        for var_name, var_value in variables.items():
            case_expr = case_expr.replace(var_name, str(var_value))
        
        return switch_expr, case_expr
    else:
        return None, None

def parse_assignment(statement, variables):
    parts = statement.split("=")
    if len(parts) == 2:
        var_name = parts[0].strip()
        var_value = parts[1].strip()

        # Si el valor es una cadena entre comillas, trátalo como tal.
        if var_value.startswith('"') and var_value.endswith('"'):
            var_value = var_value[1:-1]

        variables[var_name] = var_value

        # Ahora, también establece la variable de entorno
        set_environment_variable(var_name, var_value)
        
        return True
    else:
        return False

def set_environment_variable(var_name, var_value):
    os.environ[var_name] = var_value
    print(f"{Colors.GREEN}Variable de entorno '{var_name}' establecida a '{var_value}'.{Colors.RESET}")
    update_prompt()

def show_environment_variables(variables):
    print(f"{Colors.BLUE}Variables de entorno:{Colors.RESET}")
    for var_name, var_value in os.environ.items():
        print(f"{Colors.CYAN}{var_name} = {var_value}{Colors.RESET}")

def update_prompt():
    prompt_value = os.environ.get("PROMPT")
    if prompt_value:
        os.system(f"prompt {prompt_value}")

def run_list(commands, variables):
    for cmd in commands:
        run_command(cmd, variables)

def run_list_save(commands):
    with open("commands_list.pkl", "wb") as file:
        pickle.dump(commands, file)
    print(f"{Colors.GREEN}Lista guardada correctamente.{Colors.RESET}")

def run_list_load():
    try:
        with open("commands_list.pkl", "rb") as file:
            commands = pickle.load(file)
            print(f"{Colors.GREEN}Lista cargada correctamente.{Colors.RESET}")
            return commands
    except FileNotFoundError:
        print(f"{Colors.YELLOW}No se encontró ninguna lista guardada.{Colors.RESET}")
        return []

def run_for_loop(start, end, commands, variables):
    for i in range(start, end + 1):
        variables['i'] = i
        run_list(commands, variables)

def run_script(script_name):
    try:
        with open(script_name, "r") as script_file:
            script_content = script_file.read()
            exec(script_content)
            print(f"{Colors.GREEN}Script '{script_name}' ejecutado correctamente en modo headless.{Colors.RESET}")
    except FileNotFoundError:
        print(f"{Colors.RED}No se encontró el script '{script_name}'.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Error al ejecutar el script: {e}{Colors.RESET}")

def interactive_mode(variables):
    while True:
        user_input = input(os.environ.get("PS1") or os.environ.get("PROMPT") or f"{Colors.YELLOW}>>> {Colors.RESET}")
        
        if user_input.lower() == "exit":
            break

        if user_input.lower() == "end":
            break

        if "=" in user_input:
            if parse_assignment(user_input, variables):
                print(f"{Colors.GREEN}Variable asignada: {user_input}{Colors.RESET}")
            else:
                print(f"{Colors.RED}Error al asignar la variable. Use el formato 'variable = valor'{Colors.RESET}")
        elif user_input.lower() == "run_list":
            commands_list = []
            num_commands = int(input(f"{Colors.YELLOW}Ingrese el número de comandos que desea ingresar: {Colors.RESET}"))
            for _ in range(num_commands):
                list_command = input(f"{Colors.YELLOW}Ingrese un comando para la lista: {Colors.RESET}")
                commands_list.append(list_command)
            run_list(commands_list, variables)
        elif user_input.lower() == "run_list_save":
            run_list_save(commands_list)
        elif user_input.lower() == "run_list_load":
            commands_list = run_list_load()
            run_list(commands_list, variables)
        elif user_input.lower() == "run_for_loop":
            start = int(input(f"{Colors.YELLOW}Ingrese el valor inicial para el bucle for: {Colors.RESET}"))
            end = int(input(f"{Colors.YELLOW}Ingrese el valor final para el bucle for: {Colors.RESET}"))
            num_commands = int(input(f"{Colors.YELLOW}Ingrese el número de comandos para el bucle for: {Colors.RESET}"))
            for_commands = []
            for _ in range(num_commands):
                for_command = input(f"{Colors.YELLOW}Ingrese un comando para el bucle for: {Colors.RESET}")
                for_commands.append(for_command)
            run_for_loop(start, end, for_commands, variables)
        elif user_input.lower() == "run_script":
            script_name = input(f"{Colors.YELLOW}Ingrese el nombre del script a ejecutar en modo headless: {Colors.RESET}")
            run_script(script_name)
            break  # Salir después de ejecutar el script en modo headless.
        elif user_input.lower().startswith("set_env"):
            # Ejemplo de comando: set_env VAR_NAME::VAR_VALUE
            parts = user_input.split("::")
            if len(parts) == 2:
                var_name = parts[0].strip()[7:]  # Recorta "set_env" y elimina espacios.
                var_value = parts[1].strip()
                set_environment_variable(var_name, var_value)
            else:
                print(f"{Colors.RED}Formato incorrecto. Use el formato 'set_env VAR_NAME::VAR_VALUE'.{Colors.RESET}")
        elif user_input.lower() == "show_env":
            show_environment_variables(variables)
        else:
            switch_expr, case_expr = parse_switch_statement(user_input, variables)
            if switch_expr and case_expr:
                if eval(switch_expr, globals(), variables) == eval(case_expr, globals(), variables):
                    print(f"{Colors.GREEN}Se ejecutará el bloque case.{Colors.RESET}")
                    # Agrega aquí el código que deseas ejecutar para el bloque case.
                else:
                    print(f"{Colors.YELLOW}No se ejecutará el bloque case.{Colors.RESET}")
            else:
                if_statement = parse_if_statement(user_input, variables)
                if if_statement:
                    condition = if_statement
                    user_input = input(f"{Colors.YELLOW}Ingrese el comando a ejecutar si la condición es verdadera ({condition}): {Colors.RESET}")
                    if eval(condition, globals(), variables):
                        run_command(user_input, variables)
                    else:
                        print(f"{Colors.YELLOW}La condición es falsa. No se ejecutará el comando.{Colors.RESET}")
                else:
                    run_command(user_input, variables)

def main():
    variables = {}
    interactive_mode(variables)

if __name__ == "__main__":
    main()
