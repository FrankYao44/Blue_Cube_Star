#!/usr/bin python3
# -*- coding: utf-8 -*-
import functools
from some_useful_func import decorator_builder, next_id
from orm import Model
from orm_field import *
atom_heart_decorator = decorator_builder('url', 'subject')


def subject_detective(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        if kw['subject'] not in MCV_build_in_args['tables']:
            return 'wrong input'
        return func(*args, **kw)
    return wrapper


def _atom_heart_model_creator(subject):
    return type('AtomHeart%sDB', (Model, ),
                dict(__table__='test', id=StringField(primary_key=True, default=next_id, ddl='varchar(400)'),
                     name=StringField(ddl='varchar(400)'), subject=subject))


global _atom_heart_model_db
_atom_heart_model_db_dict = dict(zip(MCV_build_in_args['table_names'],
                                     map(_atom_heart_model_creator, MCV_build_in_args['table_names'])))


@subject_detective
@atom_heart_decorator(method='get', url='/atomheart')
async def atom_heart_init():
    print('this is a test module')
    return 'test'


@subject_detective
@atom_heart_decorator(method='get', url='/atomheart/in/{subject}/{args}')
async def write_in(subject, name):
    rs = _atom_heart_model_db[subject](name=name)
    await rs.save()
    return rs


@subject_detective
@atom_heart_decorator(method='get', url='/atomheart/out/{subject}/{args}')
async def print_out(subject, name):
    rs = _atom_heart_model_db[subject](name=name)
    await rs.findAll()
    return rs
