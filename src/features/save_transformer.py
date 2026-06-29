import joblib
from src.utils.logger import logger



def save_transformer_encoder(transformer, target_encoder, main_path="artifacts/"):

    joblib.dump(transformer, main_path + 'transformer.pkl')

    joblib.dump(target_encoder, main_path + 'label_encoder.pkl')

    logger.info(f'Feature Engineering Finished : transformer.pkl and target_encoder.pkl were saved in {main_path}')