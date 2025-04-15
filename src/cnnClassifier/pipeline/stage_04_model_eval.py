import sys
import os
sys.path.append(os.getcwd())

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval import Evaluation
from src.cnnClassifier import logger
import os
import mlflow



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/adiphalke572/my-first-repo.mlflow"
        # os.environ["MLFLOW_TRACKING_USERNAME"]="adiphalke572"
        # os.environ["MLFLOW_TRACKING_PASSWORD"]="6246c68cb22e8410de95bb97fd9851d60198fab8"

        # # set mlflow tracking URL
        # mlflow.set_tracking_uri("https://dagshub.com/adiphalke572/my-first-repo.mlflow")
        # evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e