# sqlalchemy_repr_function_create

SQLAlchemyのModelクラス作成時、すこし面倒な__init__, __repr__関数の作成を自動で行うプログラムを作成しました。
"""
class(**):
  カラム名 = ~
  カラム名 = ~
  ・
  ・
  ・
""" 
という形式の文字列を対象にしています。importなどは無視、複数クラスが記入されていてもクラスごとに作成されるようにしております。
