#ifndef _H_MATRIX
#define _H_MATRIX

#include<complex.h>
#include<tgmath.h>
#include<stdbool.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<errno.h>
#include<signal.h>

static char *msg = NULL;
static void xnr_signal_handler(int xnr_signum){
    if(xnr_signum == SIGABRT){
        perror(msg);
        free(msg);
        msg = NULL;
        exit(EXIT_FAILURE);
    }
}

typedef struct xnr_array xnr_array_t;
typedef struct xnr_matrix xnr_matrix_t;
typedef struct xnr_vector xnr_vector_t;
typedef struct xnr_shape xnr_shape_t;
typedef struct xnr_stride xnr_stride_t;
typedef struct xnr_index xnr_index_t;

typedef enum xnr_status {
    XNR_OUT_OF_RANGE_ERROR = -4,
    XNR_INCOMPATIBLE_DIMENSION = -3,
    XNR_ALLOCATION_ERROR = -2,
    XNR_INVALID = -1,
    XNR_SUCCUS = 0,
} xnr_status_t;

typedef enum xnr_dtype{
    XNR_UNKNOW_DTYPE = -1,
    XNR_INT = 1,
    XNR_LONG,
    XNR_FLOAT,
    XNR_DOUBLE,
    XNR_LONG_DOUBLE,
    XNR_COMPLEX_FLOAT,
    XNR_COMPLEX_DOUBLE,
    XNR_COMPLEX_LONG_DOUBLE,
    XNR_VECTOR,
    XNR_MATRIX,
    XNR_ARRAY,
    XNR_MESHGRID,
    XNR_MESHGRID_FLOAT,
    XNR_MESHGRID_LONG_DOUBLE,
}xnr_dtype_t;

typedef struct xnr_result{
    xnr_dtype_t dtype;
    void *result;
    const char *errmsg;
} xnr_result_t;

//
struct xnr_shape{ const int *shape; };

struct xnr_array{
    xnr_dtype_t dtype;
    xnr_shape_t *shape;
    xnr_stride_t *stride;
    int ndim;
    int size;
    void *data;
};

struct xnr_stride{
    int start;
    int stop;
    int step;
};

xnr_status_t xnr_shape_new(unsigned[], xnr_shape_t *out);
void xnr_shape_free(xnr_shape_t *);

xnr_status_t xnr_array_get_slice(
    xnr_array_t *, int axis, xnr_stride_t, xnr_result_t *result);
xnr_status_t xnr_array_set_slice(xnr_array_t *, int axis, xnr_stride_t);

/**/
xnr_status_t xnr_array_new(xnr_shape_t const *, xnr_dtype, xnr_array_t *out);
void xnr_array_free(xnr_array_t *);


xnr_status_t xnr_array_get_element(
    xnr_array_t const *, xnr_index_t const, xnr_result_t*);
xnr_status_t xnr_array_set_element(
    xnr_array_t *, xnr_index_t const, void const *value);

//
#define XNR_RESULT_FREE(resultp)                                            \
    do{                                                                     \
        if(((resultp)->data) == NULL){                                      \
            if((resultp)->errmsg != NULL){                                  \
                free((void*)((resultp)->errmsg));                           \
            }                                                               \
            return;                                                         \
        }                                                                   \
        switch((resultp)->dtype){                                           \
        case XNR_INT:                                                       \
        case XNR_LONG:                                                      \
        case XNR_FLOAT:                                                     \
        case XNR_DOUBLE:                                                    \
        case XNR_LONG_DOUBLE:                                               \
        case XNR_COMPLEX_FLOAT:                                             \
        case XNR_COMPLEX_LONG_DOUBLE:                                       \
            free((resultp)->data);                                          \
            break;                                                          \
        case XNR_VECTOR:                                                    \
            xnr_vector_free((xnr_vector_t*)((resultp)->data));              \
            break;                                                          \
        case XNR_MATRIX:                                                    \
            xnr_matrix_free((xnr_matrix_t*)((resultp)->data));              \
            break;                                                          \
        case XNR_ARRAY:                                                     \
            xnr_array_free((xnr_array_t*)((resultp)->data));                \
            break;                                                          \
        case XNR_MESHGRID:                                                  \
        case XNR_MESHGRID_FLOAT:                                            \
        case XNR_MESHGRID_LONG_DOUBLE:                                      \
            xnr_matrix_free((resultp)->data[0]);                            \
            xnr_matrix_free((resultp)->data[1]);                            \
            break;                                                          \
        default:                                                            \
            break;                                                          \
        }                                                                   \
        (resultp)->data = NULL;                                             \
        free((void*)((resultp)->errmsg));                                   \
        (resultp)->errmsg = NULL;                                           \
        (resultp)->dtype = XNR_UNKNOW_DTYPE;                                \
    }while(0)

#define XNR_GET_RESULT_VALUE(resultp, name)                                 \
    do{                                                                     \
        signal(SIGABRT, xnr_signal_handler);                                \
        if((resultp)->errmsg != NULL){                                      \
            msg = (char*)calloc(1, strlen((resultp)->errmsg)+1);            \
            strcpy(msg, (resultp)->errmsg);                                 \
            raise(SIGABRT);                                                 \
        }                                                                   \
        xnr_dtype_t dtype = (resultp)->dtype;                               \
        if(dtype == XNR_INT){                                               \
            int name = *(int*)((resultp)->data);                            \
        }else if(dtype == XNR_LONG){                                        \
            long name = *(long*)((resultp)->data);                          \
        }else if(dtype == XNR_FLOAT){                                       \
            float name = *(float*)((resultp)->data);                        \
        }else if(dtype == XNR_DOUBLE){                                      \
            double name = *(double*)((resultp)->data);                      \
        }else if(dtype == XNR_LONG_DOUBLE){                                 \
            long double name = *(long double*)((resultp)->data);            \
        }else if(dtype == XNR_COMPLEX_FLOAT){                               \
            float x = creal(*(float complex*)((resultp)->data));            \
            float y = cimag(*(float complex*)((resultp)->data));            \
            float complex name = CMPLXF(x, y)                               \
        }else if(dtype == XNR_COMPLEX_DOUBLE){                              \
            double x = creal(*(double complex*)((resultp)->data));          \
            double y = cimag(*(double complex*)((resultp)->data));          \
            double complex name = CMPLX(x, y);                              \
        }else if(dtype == XNR_COMPLEX_LONG_DOUBLE){                         \
            long double x = creal(*(long double complex*)((resultp)->data));\
            long double y = cimag(*(long double complex*)((resultp)->data));\
            double complex name = CMPLXL(x, y);                             \
        }else if(dtype == XNR_VECTOR){                                      \
            xnr_vector_t* name = ((xnr_vector_t*)(resultp)->data);          \
        }else if(dtype == XNR_MATRIX){                                      \
            xnr_matrix_t* name = (xnr_matrix_t*)((resultp)->data);          \
        }else if(dtype == XNR_ARRAY){                                       \
            xnr_array_t* name = (xnr_matrix_t*)((resultp)->data);           \
        }else if(dtype == XNR_MESHGRID){                                    \
            void *__data = (resultp)->data;                                 \
            double  *x ## name = ((double*)__data)[0];                      \
            double  *y ## name = ((double*)__data)[1];                      \
        }else if(dtype == XNR_MESHGRID_FLOAT){                              \
            void *__data = (resultp)->data;                                 \
            float  *x ## name = ((float*)__data)[0];                        \
            float  *y ## name = ((float*)__data)[1];                        \
        }else if(dtype == XNR_MESHGRID_LONG_DOUBLE){                        \
            void *__data = (resultp)->data;                                 \
            long double  *x ## name = ((long double*)__data)[0];            \
            long double  *y ## name = ((long double*)__data)[1];            \
        }                                                                   \
    }while(0)


/*----------------------------------------------------------------------*/
// VECTOR
xnr_status_t xnr_vector_new(int n, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_vector_free(xnr_vector_t *vec);
xnr_status_t xnr_vector_print(
    xnr_vector_t const *vec, char const *fmt);
xnr_status_t xnr_vector_copy(xnr_vector_t const *vec, xnr_result *result);
xnr_status_t xnr_vector_length(xnr_vector_t const *self, xnr_result *result);
xnr_status_t xnr_vector_get(
    xnr_vector_t const *self, int index, xnr_result_t *result);
xnr_status_t xnr_vector_set(
    xnr_vector_t *self, int index, const void *value);
xnr_status_t xnr_vector_get_slice(
    xnr_vector_t *, int axis, xnr_stride_t, xnr_result_t *result);
xnr_status_t xnr_vector_set_slice(xnr_vector_t *, int axis, xnr_stride_t);

xnr_status_t xnr_vector_add(
    xnr_vector_t *lhs, xnr_vector_t *rhs, xnr_result_t *result);
xnr_status_t xnr_vector_sub(
    xnr_vector_t *lhs, xnr_vector_t *rhs, xnr_result_t *result);
xnr_status_t xnr_vector_mul(
    xnr_vector_t *lhs, xnr_vector_t *rhs, xnr_result_t *result);

xnr_status_t xnr_vector_add_scalar(
    xnr_vector_t *lhs, void const *scalar, xnr_result_t *result);
xnr_status_t xnr_vector_sub_scalar(
    xnr_vector_t *lhs, void const *scalar, xnr_result_t *result);
xnr_status_t xnr_vector_mul_scalar(
    xnr_vector_t *lhs, void const *scalar, xnr_result_t *result);

xnr_status_t xnr_dot_product(
    xnr_vector_t const *lhs,
    xnr_vector_t const *rhs,
    xnr_result *result);

xnr_status_t xnr_vector_apply(
    xnr_vector_t *lhs, void*(*fn)(void*), xnr_result *result);
xnr_status_t xnr_vector_map(
    xnr_vector_t *lhs, xnr_vector_t *rhs,
    void*(*fn)(void*, void*), xnr_result *result);
xnr_status_t xnr_vector_reduce(
    xnr_vector_t const *lhs, void*(*fn)(void *, void*), xnr_result_t *result);
xnr_status_t xnr_vector_filter(
    xnr_vector_t const *lhs, bool (*predicate)(void*, void*),
    xnr_result_t *result);
xnr_status_t xnr_vector_norm(xnr_vector_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_vector_normalize(
    xnr_vector_t const *lhs, xnr_result_t *result);

xnr_status_t xnr_vector_zeros(int n, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_vector_ones(int n, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_vector_maxval(xnr_vector_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_vector_minval(xnr_vector_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_vector_mean(xnr_vector_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_vector_stdev(xnr_vector_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_vector_correlation(
    xnr_vector_t const *lhs, xnr_vector_t const* rhs, xnr_result_t *result);
xnr_status_t xnr_linspace(
    double start, double stop, int size, xnr_result_t *result);
xnr_status_t xnr_arange(
    double start, double stop, double step, xnr_result_t *result);


/*----------------------------------------------------------------------*/
// MATRIX
xnr_status_t xnr_matrix_new(
    int nrow, int ncol, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_matrix_free(xnr_matrix_t *mat);
void xnr_matrix_print(
    xnr_matrix_t const *mat, char const *fmt, char const *delim);
xnr_status_t xnr_matrix_copy(xnr_matrix_t const *mat, xnr_result *result);
xnr_status_t xnr_matrix_get(
    xnr_matrix_t const *self, int row, int col, xnr_result_t *result);
xnr_status_t xnr_matrix_set(
    xnr_matrix_t *self, int row, int col, const void *value);
xnr_status_t xnr_matrix_get_slice(
    xnr_matrix_t *self, int axis, xnr_stride_t stride, xnr_result_t *result);
xnr_status_t xnr_matrix_set_slice(
    xnr_matrix_t *self, int axis, xnr_stride_t stide);
xnr_status_t xnr_matrix_get_rowvec(
    xnr_matrix_t *self, int irow, xnr_result_t* result);
xnr_status_t xnr_matrix_get_colvec(
    xnr_matrix_t *self, int icol, xnr_result_t* result);

xnr_status_t xnr_matrix_length(xnr_matrix_t const *self, xnr_result *result);
xnr_status_t xnr_matrix_nrow(xnr_matrix_t const *self, xnr_result *result);
xnr_status_t xnr_matrix_ncolumn(xnr_matrix_t const *self, xnr_result *result);
xnr_status_t xnr_matrix_shape(xnr_matrix_t const *self, xnr_result *result);


xnr_status_t xnr_matrix_add(
    xnr_matrix_t const *lhs, xnr_matrix_t const *rhs, xnr_result_t *result);
xnr_status_t xnr_matrix_sub(
    xnr_matrix_t const *lhs, xnr_matrix_t const *rhs, xnr_result_t *result);
xnr_status_t xnr_matrix_mul(
    xnr_matrix_t const *lhs, xnr_matrix_t const *rhs, xnr_result_t *result);

xnr_status_t xnr_matrix_add_scalar(
    xnr_matrix_t const *lhs, void const *scalar, xnr_result_t *result);
xnr_status_t xnr_matrix_sub_scalar(
    xnr_matrix_t const *lhs, void const *scalar, xnr_result_t *result);
xnr_status_t xnr_matrix_mul_scalar(
    xnr_matrix_t const *lhs, void const *scalar, xnr_result_t *result);

xnr_status_t xnr_matrix_apply(
    xnr_matrix_t *lhs, void*(*fn)(void*), xnr_result *result);
xnr_status_t xnr_matrix_map(
    xnr_matrix_t *lhs, xnr_matrix_t *rhs,
    void*(*fn)(void*, void*), xnr_result *result);
xnr_status_t xnr_matrix_reduce(
    xnr_matrix_t const *lhs, void*(*fn)(void *, void*), xnr_result_t *result);
xnr_status_t xnr_matrix_filter(
    xnr_matrix_t const *lhs, bool (*predicate)(void*, void*),
    xnr_result_t *result);

xnr_status_t xnr_matrix_zeros(
    int nrow, int ncol, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_matrix_ones(
    int nrow, int ncol, xnr_dtype_t dtype, xnr_result *result);
xnr_status_t xnr_matrix_maxval(xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_minval(xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_meshgrid(xnr_matrix_t const *lhs, xnr_result_t *result);

xnr_status_t xnr_matrix_normalize(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_transpose(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_trace(xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_det(xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_identity(int n, xnr_result_t *result);
xnr_status_t xnr_diag(xnr_vector_t const *vec, xnr_result_t *result);
xnr_status_t xnr_matrix_get_diagonal(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_is_square(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_is_upper_triangular(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_is_lower_triangular(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_svd(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_lu(
    xnr_matrix_t const *lhs, xnr_result_t *result);
xnr_status_t xnr_matrix_qr(
    xnr_matrix_t const *lhs, xnr_result_t *result);

/*------------------------------------------------------------------------*/
FILE* xnr_fopen(char const *filename, char const *mode);
size_t xnr_fclose(FILE* stream);
size_t xnr_array_fprintf(
    FILE *stream, char const* fmt, char const *delim, xnr_array_t const *data);
size_t xnr_vector_fprintf(
    FILE *stream, char const* fmt, char const *delim, xnr_vector_t const *data);
size_t xnr_matrix_fprintf(
    FILE *stream, char const* fmt, char const *delim, xnr_matrix_t const *data);
size_t xnr_array_fscanf(
    FILE *stream, char const* fmt, xnr_array_t *data);
size_t xnr_vector_fscanf(
    FILE *stream, char const* fmt, xnr_vector_t *data);
size_t xnr_matrix_fscanf(
    FILE *stream, char const* fmt, xnr_matrix_t *data);
size_t xnr_array_fread(
    FILE *stream, char const* fmt, xnr_array_t const *data);
size_t xnr_vector_fread(
    FILE *stream, char const* fmt, xnr_vector_t const *data);
size_t xnr_matrix_fread(
    FILE *stream, char const* fmt, xnr_matrix_t const *data);
size_t xnr_array_fwrite(
    FILE *stream, char const* fmt, xnr_array_t const *data);
size_t xnr_vector_fwrite(
    FILE *stream, char const* fmt, xnr_vector_t const *data);
size_t xnr_matrix_fwrite(
    FILE *stream, char const* fmt, xnr_matrix_t *data);

//
#endif
