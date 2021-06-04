from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Badges(Resource):
    """ Gets all badges """
    def get(self):
        response = list(database.db.Badges.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])
        
        return jsonify(response)

    def post(self):
        _ids = list(database.db.Badges.insert_many([
            {
            'name':request.json[0]['name'],
            'last_name':request.json[0]['last_name'],
            'profile_picture':request.json[0]['profile_picture'],
            'hero_badge':request.json[0]['hero_badge'],
            'age':request.json[0]['age'],
            'city':request.json[0]['city'],
            'followers':request.json[0]['followers'],
            'likes':request.json[0]['likes'],
            'pictures':request.json[0]['pictures'],
            },
            {
            'name':request.json[1]['name'],
            'last_name':request.json[1]['last_name'],
            'profile_picture':request.json[1]['profile_picture'],
            'hero_badge':request.json[1]['hero_badge'],
            'age':request.json[1]['age'],
            'city':request.json[1]['city'],
            'followers':request.json[1]['followers'],
            'likes':request.json[1]['likes'],
            'pictures':request.json[1]['pictures'],
            },
            {
            'name':request.json[2]['name'],
            'last_name':request.json[2]['last_name'],
            'profile_picture':request.json[2]['profile_picture'],
            'hero_badge':request.json[2]['hero_badge'],
            'age':request.json[2]['age'],
            'city':request.json[2]['city'],
            'followers':request.json[2]['followers'],
            'likes':request.json[2]['likes'],
            'pictures':request.json[2]['pictures'],
            },
            {
            'name':request.json[3]['name'],
            'last_name':request.json[3]['last_name'],
            'profile_picture':request.json[3]['profile_picture'],
            'hero_badge':request.json[3]['hero_badge'],
            'age':request.json[3]['age'],
            'city':request.json[3]['city'],
            'followers':request.json[3]['followers'],
            'likes':request.json[3]['likes'],
            'pictures':request.json[3]['pictures'],
            },
            {
            'name':request.json[4]['name'],
            'last_name':request.json[4]['last_name'],
            'profile_picture':request.json[4]['profile_picture'],
            'hero_badge':request.json[4]['hero_badge'],
            'age':request.json[4]['age'],
            'city':request.json[4]['city'],
            'followers':request.json[4]['followers'],
            'likes':request.json[4]['likes'],
            'pictures':request.json[4]['pictures'],
            },
            {
            'name':request.json[5]['name'],
            'last_name':request.json[5]['last_name'],
            'profile_picture':request.json[5]['profile_picture'],
            'hero_badge':request.json[5]['hero_badge'],
            'age':request.json[5]['age'],
            'city':request.json[5]['city'],
            'followers':request.json[5]['followers'],
            'likes':request.json[5]['likes'],
            'pictures':request.json[5]['pictures'],
            },
            {
            'name':request.json[6]['name'],
            'last_name':request.json[6]['last_name'],
            'profile_picture':request.json[6]['profile_picture'],
            'hero_badge':request.json[6]['hero_badge'],
            'age':request.json[6]['age'],
            'city':request.json[6]['city'],
            'followers':request.json[6]['followers'],
            'likes':request.json[6]['likes'],
            'pictures':request.json[6]['pictures'],
            },
            {
            'name':request.json[7]['name'],
            'last_name':request.json[7]['last_name'],
            'profile_picture':request.json[7]['profile_picture'],
            'hero_badge':request.json[7]['hero_badge'],
            'age':request.json[7]['age'],
            'city':request.json[7]['city'],
            'followers':request.json[7]['followers'],
            'likes':request.json[7]['likes'],
            'pictures':request.json[7]['pictures'],
            },
            {
            'name':request.json[8]['name'],
            'last_name':request.json[8]['last_name'],
            'profile_picture':request.json[8]['profile_picture'],
            'hero_badge':request.json[8]['hero_badge'],
            'age':request.json[8]['age'],
            'city':request.json[8]['city'],
            'followers':request.json[8]['followers'],
            'likes':request.json[8]['likes'],
            'pictures':request.json[8]['pictures'],
            },
            {
            'name':request.json[9]['name'],
            'last_name':request.json[9]['last_name'],
            'profile_picture':request.json[9]['profile_picture'],
            'hero_badge':request.json[9]['hero_badge'],
            'age':request.json[9]['age'],
            'city':request.json[9]['city'],
            'followers':request.json[9]['followers'],
            'likes':request.json[9]['likes'],
            'pictures':request.json[9]['pictures'],
            },
            
        ]).inserted_ids)


        results = []

        for _id in _ids:
            results.append(str(_id))
            
        return jsonify({'inserted_ids':results})
    
    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count