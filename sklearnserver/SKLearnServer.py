import joblib
import numpy as np
import seldon_core
from seldon_core.user_model import SeldonComponent, SeldonResponse
from typing import Dict, List, Union, Iterable
import os
import logging
import yaml

logger = logging.getLogger(__name__)

JOBLIB_FILE = "regression.joblib"


class SKLearnServer(SeldonComponent):
    def __init__(self, model_uri: str = None, method: str = "predict"):
        super().__init__()
        self.model_uri = model_uri
        self.method = method
        self.ready = False
        logger.info(f"Model uri: {self.model_uri}")
        logger.info(f"method: {self.method}")
        self.last_predict = None

        self.load()

    def load(self):
        logger.info("load")
        model_file = os.path.join(
            seldon_core.Storage.download(self.model_uri), JOBLIB_FILE
        )
        logger.info(f"model file: {model_file}")
        self._joblib = joblib.load(model_file)
        self.ready = True

    def predict(
        self, X: np.ndarray, names: Iterable[str], meta: Dict = None
    ) -> Union[np.ndarray, List, str, bytes]:
        try:
            if not self.ready:
                self.load()
                
            logger.info("Calling predict")
            result = self._joblib.predict(X)
            self.last_predict = result
            
            return SeldonResponse(data=result)
            
        except Exception as ex:
            logging.exception("Exception during predict")
            
    def metrics(self):
        return [{"type": "GAUGE", "key": "prva_kutija", "value": self.last_predict[0].tolist()}, {"type": "GAUGE", "key": "druga_kutija", "value": self.last_predict[1].tolist()}, {"type": "GAUGE", "key": "treca_kutija", "value": self.last_predict[2].tolist()}, {"type": "GAUGE", "key": "cetvrta_kutija", "value": self.last_predict[3].tolist()}, {"type": "GAUGE", "key": "peta_kutija", "value": self.last_predict[4].tolist()}, ]
