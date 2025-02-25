# automech-repair
AutoMech Repair System is an ERP solution that transforms the automobile repair industry. It uses computer vision for improved diagnostics and automates repair processes. With cloud-based infrastructure for secure image storage, it provides efficient management and seamless access to repair data, benefiting both repair shops and customers

##  Tech Stack
###  Backend
- **Flask** (REST API)
- **Flask-SQLAlchemy** (SQLite3 database)
- **EfficientNet (TensorFlow/PyTorch)** (Spare part recognition)
- **Firebase** (Cloud image storage)
- **JWT Authentication** (User authentication & access control)

### Frontend
- **React.js** (UI framework)
- **Bootstrap** (Styling & responsiveness)
- **Axios** (API integration)
- **React Router** (Navigation)

###  Cloud Services
- **Firebase Storage** (Store spare part images)
- **Google Cloud / Heroku** (Backend deployment)
- **Netlify / Vercel** (Frontend hosting)

## Features
 **Spare Part Identification:** Uses EfficientNet to classify spare parts based on uploaded images.  
 **Cloud Storage:** Uploads unidentified spare parts to Firebase.  
 **Repair Requests:** Customers can submit repair requests with part images.  
 **Supplier Management:** Suppliers can add and manage inventory.  
 **User Roles:** Authentication for mechanics, suppliers, and customers.  
 **Admin Mechanic Role:** A designated mechanic with admin privileges to oversee operations and manage users.  
 **Inventory Management:** Track spare parts and supplies.  
 **Customer Notifications:** Send SMS/Email alerts for job updates and reminders.  
 **Reporting & Analytics:** Generate reports on job history, expenses, and performance.  

##  Installation & Setup
###  Backend Setup
# Clone the repository
git clone git@github.com:Nakecy/automech-repair.git
cd autorepair-erp

# Set up a virtual environment
pip install pipenv
pipenv shell

# Install dependencies
pip install -r requirements.txt

# Run Flask app
flask run

### Frontend Setup
cd client
npm install
npm start

##  API Endpoints
###  Authentication & User Management
| Endpoint               | Method | Description |
|------------------------|--------|-------------|
| `/api/auth/signup`     | POST   | User registration |
| `/api/auth/login`      | POST   | User login (JWT) |
| `/api/admin/users`     | GET    | Admin retrieves user list |
| `/api/admin/promote`   | POST   | Promote a mechanic to admin |

###  Spare Parts & Inventory
| Endpoint               | Method | Description |
|------------------------|--------|-------------|
| `/api/parts/upload`    | POST   | Upload spare part image |
| `/api/parts/identify`  | POST   | Run EfficientNet model |
| `/api/parts/list`      | GET    | Fetch spare parts catalog |
| `/api/parts/update`    | PUT    | Update spare part details |
| `/api/inventory/stock` | GET    | Retrieve current inventory |
| `/api/inventory/add`   | POST   | Add new spare parts |

###  Repair Requests
| Endpoint               | Method | Description |
|------------------------|--------|-------------|
| `/api/requests/new`    | POST   | Create a repair request |
| `/api/requests/status` | GET    | Get repair request status |
| `/api/requests/update` | PUT    | Update repair request status |

###  Notifications & Reports
| Endpoint               | Method | Description |
|------------------------|--------|-------------|
| `/api/notifications/send` | POST  | Send SMS/Email notifications |
| `/api/reports/generate`  | GET   | Generate analytics reports |

##  Database Schema (SQLite3)
###  Users Table
- `id` (Primary Key)
- `name`
- `email`
- `password`
- `role` (customer, mechanic, supplier, admin)

###  Spare Parts Table
- `id` (Primary Key)
- `name`
- `image_url` (Firebase link)
- `category`
- `supplier_id` (Foreign Key)
- `stock_quantity`

###  Repair Requests Table
- `id` (Primary Key)
- `customer_id` (Foreign Key)
- `spare_part_id` (Foreign Key)
- `status` (pending, completed)
- `mechanic_id` (Foreign Key)

###  Notifications Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `message`
- `sent_at`

##  Testing
- Use **Postman** for API testing.
- Run **unit tests** with `pytest`.
- Frontend testing with **Jest**.

##  Deployment
1. Deploy Flask backend on **Google Cloud Run** or **Heroku**.
2. Host frontend on **Netlify** or **Vercel**.
3. Configure Firebase for **image storage**.

##  Future Enhancements
- **E-commerce Features:** Allow spare part purchases.
- **AI Model Optimization:** Improve accuracy with more training data.
- **Dashboard:** Add analytics for mechanics & suppliers.

## Contributors
1.Obed Omayio
2.Alvine Allan

##  License
This project is open-source and available under the **MIT License**.



