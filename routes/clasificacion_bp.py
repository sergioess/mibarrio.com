from flask import Blueprint

# from controllers.ClasificacionController import index, store, show, update, destroy, create, edit
from controllers.ClasificacionControllerPst import index, store, show, update, destroy, create, edit

clasificacion_bp = Blueprint('clasificacion_bp', __name__, template_folder='templates/clasificacion')
clasificacion_bp.route('/', methods=['GET'])(index)
clasificacion_bp.route('/create', methods=['GET'])(create)
clasificacion_bp.route('edit/<int:clasificacion_id>', methods=['GET'])(edit)
clasificacion_bp.route('/store', methods=['POST'])(store)
clasificacion_bp.route('/<int:clasificacion_id>', methods=['GET'])(show)
clasificacion_bp.route('/update', methods=['POST'])(update)
clasificacion_bp.route('/destroy/<int:clasificacion_id>',methods=['GET', 'POST', 'DELETE'])(destroy)
