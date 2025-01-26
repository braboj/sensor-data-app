#encoding: utf-8
"""
Database module

This module defines the database object. It is required in order to avoid
circular imports. The database object is instantiated in the app factory
function in the app module.

In the future, this module could be used to implement database handling
functions, such as database initialization, cleanup, and migrations.
"""

from flask_sqlalchemy import SQLAlchemy

# Global database object
db = SQLAlchemy()