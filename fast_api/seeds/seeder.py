import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder

from core.config import SEEDS_PATH, SEEDS_TOPICS
from db.sa_db import engine

logger = logging.getLogger(__name__)


def seed_db():
    with Session(engine) as session:
        seeder = Seeder(session)
        logger.info('Starting seeding the database')
        for topic in SEEDS_TOPICS:
            file_path = SEEDS_PATH + topic + '.json'
            entities = load_entities_from_json(file_path)
            try:
                logger.info(f'Seeding the topic: {topic}')
                seeder.seed(entities)
                session.commit()
                logger.info(f'Topic {topic} was seeded')
            except IntegrityError:
                logger.info(f"It's look like the topic {topic} already been seeded")
                return
