from fastapi import Depends, FastAPI
from database import get_db, engine
from sqlalchemy.orm import Session
from entities.many_to_one_uni.post_entity import PostEntity
from entities.many_to_one_uni.student_entity import StudentEntity
from entities.one_to_many_uni.child_entity import ChildEntity
from entities.one_to_many_uni.parent_entity import ParentEntity
from entities.entity_base import EntityBase
from entities.one_to_many_bi.ChildEntityBidirectional import ChildEntityBidirectional
from entities.one_to_many_bi.ParentEntityBidirectional import ParentEntityBidirectional
from entities.many_to_many_uni.event_entity import EventEntity
from entities.many_to_many_uni.user_entity import UserEntity
from entities.many_to_many_bi.customer_entity import CustomerEntity
from entities.many_to_many_bi.product_entity import ProductEntity

EntityBase.metadata.drop_all(bind=engine)
EntityBase.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/one-to-many-uni")
def entities(session : Session = Depends(get_db)):
    a_child : ChildEntity = ChildEntity(
        name = "Charles")
    other_child: ChildEntity = ChildEntity(
        name = "Sadie")
    parent : ParentEntity = ParentEntity(
        name = "Parent",
        children = [a_child, other_child])
    session.add(a_child)
    session.add(other_child)
    session.add(parent)
    session.commit()
    return "works!"

@app.get("/one-to-many-uni")
def get_entities(session: Session = Depends(get_db)):
    parents = session.query(ParentEntity).all()
    children = [parent.children for parent in parents] 
    return parents

@app.post("/many-to-one-uni")
def create_posts(session: Session = Depends(get_db)):
    student :  StudentEntity = StudentEntity(
        name = "Charles")
    post : PostEntity = PostEntity(
        content = "Hello World",
        student_id = student.id,
        student = student)
    other_student : StudentEntity = StudentEntity(
        name = "Sadie")
    other_post : PostEntity = PostEntity(
        content = "OH is so long!",
        student_id = other_student.id,
        student = other_student)

    session.add(student)
    session.add(other_student)
    session.add(other_post)
    session.add(post)
    session.commit()

@app.get("/many-to-one-uni")
def get_posts(session: Session = Depends(get_db)):
    posts = session.query(PostEntity).all()
    students = [post.student for post in posts]
    return posts

@app.post("/one-to-many-bi")
def create_parents_children(session: Session = Depends(get_db)):
    a_child : ChildEntity = ChildEntityBidirectional(
        name = "Charles")
    other_child: ChildEntity = ChildEntityBidirectional(
        name = "Sadie")
    parent : ParentEntity = ParentEntityBidirectional(
        name = "Kris",
        children = [a_child, other_child]) 
    session.add(a_child)
    session.add(other_child)
    session.add(parent)
    session.commit()
    return "works!"

@app.get("/one-to-many-bi")
def get_children_from_parents_bidirectional(session: Session = Depends(get_db)):
    parents = session.query(ParentEntityBidirectional).all()
    children = [parent.children for parent in parents]
    return parents

@app.get("/one-to-many-bi/parent")
def get_parents_from_children_bidirectional(session: Session = Depends(get_db)):
    children = session.query(ChildEntityBidirectional).all()
    parents = [child.parent for child in children]
    return parents

@app.post("/many-to-many-uni")
def create_events_and_users(session: Session = Depends(get_db)):
    a_user : UserEntity = UserEntity(
        name = "Fernando")
    other_user : UserEntity = UserEntity(
        name = "Fabio")
    session.add(a_user)
    session.add(other_user)
    session.commit()
    event : EventEntity = EventEntity(
        name = "Party",
        users = [a_user, other_user])
    session.add(event)
    session.commit()

@app.get("/many-to-many-uni")
def get_users_from_events(session: Session = Depends(get_db)):
    events = session.query(EventEntity).all()
    users = [event.users for event in events]
    return events

@app.get("/many-to-many-uni/event")
def get_events_from_users(session: Session = Depends(get_db)):
    event = session.query(EventEntity).first()
    return event 

@app.post("/many-to-many-bi")
def create_customers_and_products(session: Session = Depends(get_db)):
    customer : CustomerEntity = CustomerEntity(
       name="Kris" 
    )
    other_customer : CustomerEntity = CustomerEntity(
        name="Fernando"
    )
    session.add(customer)
    session.add(other_customer)
    session.commit()
    product : ProductEntity = ProductEntity(
        name = "Laptop",
        customers = [customer, other_customer]
    )
    other_product : ProductEntity = ProductEntity(
        name = "Car",
        customers = [customer, other_customer]
    )
    session.add(product)
    session.add(other_product)
    session.commit()

@app.get("/many-to-many-bi")
def get_customers_from_products(session: Session = Depends(get_db)):
    products = session.query(ProductEntity).all()
    customers = [product.customers for product in products]
    return products

@app.get("/many-to-many-bi/products")
def get_products_from_customers(session: Session = Depends(get_db)):
    customers = session.query(CustomerEntity).all()
    products = [customer.products for customer in customers]
    return customers
