#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        
        print('Deleting existing birds...')
        User.query.delete()

        print('Creating bird objects...')
        users = []
        user1 = User(
            username='lightyagami',
            email='lightyagami@gmail.com',
            first_name='Light',
            last_name='Yagami',
            profile_pic='https://i.imgur.com/q4IgIRx.png'
        )
        users.append(user1)
        user2 = User(
            username='roronoazoro',
            email='roronoazoro@gmail.com',
            first_name='Roronoa',
            last_name='Zoro',
            profile_pic='https://i.imgur.com/XcxCRIW.png'
        )
        users.append(user2)

        print('Adding bird objects to transaction...')
        db.session.add_all(users)

        print('Committing transaction...')
        db.session.commit()

        print('Complete.')
