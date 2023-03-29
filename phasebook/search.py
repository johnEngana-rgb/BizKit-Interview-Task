from flask import Blueprint, request
import re 
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200



def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Create a list to store the matching users
    matches = []

    # Loop through the users and check if they match the search criteria
    for user in USERS:
        matched = True
        for arg, value in args.items():
            if arg == "id" and value != user["id"]:
                matched = False
                break
            if arg == "name" and value.lower() not in user["name"].lower():
                matched = False
                break
            if arg == "age":
                age = int(value)
                if not (age - 1 <= user["age"] <= age + 1):
                    matched = False
                    break
            if arg == "occupation" and value.lower() not in user["occupation"].lower():
                matched = False
                break
        if matched:
            matches.append(user)

    return matches