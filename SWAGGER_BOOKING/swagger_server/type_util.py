#
# type_util.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import sys
if sys.version_info < (3, 7):
    import typing

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return type(klass) == typing.GenericMeta

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__extra__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__extra__ == list

else:

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return hasattr(klass, '__origin__')

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__origin__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__origin__ == list
