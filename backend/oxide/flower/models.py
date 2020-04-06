import factory

from oxide.core.extensions import db, ma


class Flower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    latin_name = db.Column(db.String(120), index=True, unique=True)
    genus = db.Column(db.String(128))

    def __repr__(self):
        return "<Flower {}>".format(self.name)


class FlowerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Flower
        load_instance = True
        sqla_session = db.session

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field()
    latin_name = ma.auto_field()
    genus = ma.auto_field()


class FlowerFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Flower
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: "%s" % n)
    name = factory.Faker("color")
    latin_name = factory.Faker("color")
    genus = factory.Faker("color")


flower_schema = FlowerSchema()
flowers_schema = FlowerSchema(many=True)
