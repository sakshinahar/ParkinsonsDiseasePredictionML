from urllib import request
from flask import *
from flask import render_template
from flask import jsonify
import pickle
import numpy as np
import telebot
import os




load_model_DT=pickle.load(open('./static/Sav_Models/DT_model.sav','rb'))
load_model_KNN=pickle.load(open('./static/Sav_Models/KNN_model.sav','rb'))
load_model_RF=pickle.load(open('./static/Sav_Models/RF_model.sav','rb'))
load_model_XG=pickle.load(open('./static/Sav_Models/GB_model.sav','rb'))

TOKEN = '6161309317:AAE8v7STJuBedd33NnCmtTrGauLFwm0vc1w'
FILE_PATH = os.path.join('static','images')
AUDIO_PATH = os.path.join('static','audio')


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def intro(message):
    user_name = message.chat.username
    bot.reply_to(message,f'👋 Hello {user_name} ! \nI\'m a PDML BOT🤖 abbrevated as Parkionson\'s Diesease Prediction Using Machine Learning Algorithms. \n\n\nOur Servicesfor Prediction of Parkinson\'s Disease,\n\n1). High Accurate ML Algorithms:Know the results instantly using Supervised Machine Learning Algorithms with high accuracy\n\n2). Audio\n\n3). Spiral Drawning:Predict the disease not only using vocal features but also by uploading the spiral drawings. \n\n\n Get Started \n\n/pmdldata : For High Accurate ML Algorithms(Note: You have to Enter the Data)\n\n/pmdlvoice : Send the Audio file to bot in mp3,mp4 format.\n\n/pmdlspiral : Send Spiral Drwanings to the bot in jpeg,jpj format.')


# help command
@bot.message_handler(commands=['help'])
def helper(message):
    bot.reply_to(message,'Try typing anything and I will do my best to respond!')


@bot.message_handler(content_types=['text'])
def text_input(message):
    text_input = message.text
    text_input_list = text_input.split(",")
    if len(text_input_list) == 22:
        float_list = []
        for s in text_input_list:
            try:
                f = float(s)
                float_list.append(f)
                
            except ValueError:
                return'No Characters are allowed:'.format(s)
        #print(float_list)
        #return'hi{}'.format(float_list)
        #write machine Learning code for 22 features
        # changing input data to a numpy array
        input_data = (float_list)
        #print(input_data)
        input_data_as_numpy_array = np.asarray(float_list)

        # reshape the numpy array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the data
        #std_data = scaler.transform(input_data_reshaped)

        prediction_DT = load_model_DT.predict(input_data_reshaped)
        print(prediction_DT)
        prediction_KNN = load_model_KNN.predict(input_data_reshaped)
        print(prediction_KNN)
        prediction_RF = load_model_RF.predict(input_data_reshaped)
        print(prediction_RF)
        prediction_XG = load_model_XG.predict(input_data_reshaped)
        print(prediction_XG)
        bot.reply_to(message,'Result XG{} KNN{} DT{},RF{}'.format(prediction_XG,prediction_KNN,prediction_DT,prediction_RF))
    if len(text_input_list) != 22:
        return 'it has only {} features'.format(len(text_input_list))
    if len(text_input_list) > 22:
        return 'it has {} features '.format(len(text_input_list))
    

@bot.message_handler(content_types=['photo'])
def document_image_download(message):
    # document download
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    document_path = os.path.join('static','images','Image.jpg')
    with open(document_path, "wb") as f:
        f.write(downloaded_file)
    bot.reply_to(message,"Image Downloaded")

@bot.message_handler(content_types=['audio'])
def document_audio_download(message):
    # document download
    
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    document_path = os.path.join('static','audio','audio.wav')
    with open(document_path, "wb") as f:
        f.write(downloaded_file)
    bot.reply_to(message,"Audio Downloaded")

    

if __name__ == "__main__":
    bot.polling()
